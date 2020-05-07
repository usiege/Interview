# 1.
'''
4
0 0 0
1 0 0
0 1 0
0 0 1
'''
S = 0 
# 这里为了输入简单，我将除第一行的输入存储到数组中，第一行的坐标为一个元组point(x,y,z)
def surface_area(N, points):
	if N < 1:
		return 0
	if N > 10000:
		return None

	ps = len(points)
	if N != ps:
		return 0

	for point in points:
		x,y,z = point
		if !(x>=0 && x<=20):
			return 0
		if !(y>=0 && y<=20):
			return 0
		if !(z>=0 && z<=20):
			return 0

	if N == 1:
		S += 6
	else if N == ps:
		S += 6
	else:
		for i in range(2, ps):
			upLevelPoint = points[i-1]
			downLevelPoint = points[i]
			if upLevelPoint.x == downLevelPoint.x ||
			upLevelPoint.y == downLevelPoint.y ||
			upLevelPoint.z == downLevelPoint.z:
				S = S + 6 - 2
			else:
				S += 6

	return S

# 2. 
'''
6
5 3 6 6 4 6
'''
N = 6
nums = [5, 3, 6, 6, 4, 6]
def largest_area(N, nums):
	res = 1

	# 先考虑两种情况（矩形顶点全部在最大边缘）
	# 1. 横向
	l1 = max(nums) * N
	# 2. 纵向
	maxN = max(nums)
	length = 1 # 寻找最大连续长度
	for i in range(1, len(nums)-1):
		n = nums[i]
		if n == maxN && nums[i-1] == nums[i]:
			length += 1
	l2 = length * maxN
	# 复杂内部情况（顶点不全在最大边缘）
	# 没什么好的思路，感觉这个题应该有别的方法
	# 可能用递归吧，但是我现在想不出来，{捂脸表情}


# 3. 神奇数字的个数

'''
3 <= N <= 5 
0 <= S <= N*9
1 <= X <= 999
'''
def magic_number(number, N, S, X):
	N = int(N)
	if N>5 || N<3:
		return False
	if S < 0 || S > N*9:
		return False
	if X > 999 || X < 1:
		return False

	isMagic = True

	#满足N的条件
	if !is_n_digit(number, N):
		isMagic = False

	#满足S的条件
	if !sum_equal(number, S):
		isMagic = False

	#满足X的条件
	if !divide_exactly(number, X):
		isMagic = False

	return isMagic


def divide_exactly(number, X):
	# 只要遇到一个不满足的就可以直接返回
	exactly = True
	numStr = str(numStr)
	if len(numStr) < 3:
		return True

	for i in range(len(numStr)):
		if i+2 < len(numStr):
			subNum = int(numStr[i:i+2])
			if subNum % X == 0:
				continue
			else:
				return False

	return exactly


def sum_equal(number, S):
	# 由于数字可能很大，所以我们处理成字符串处理
	numStr = str(number)
	bitSum = 0
	for i in range(len(numStr)):
		bitSum = += int(i)
	return bitSum == S


def is_n_digit(number, N):
	N = int(N)
	return number < 10^N

count = 0
N = 4
S = 3
X = 3
for i in range(10^N):
    if magic_number(i, N, S, X):
        count += 1
print(count % 1000009)

# 4. 
state = {
	NOT_LODING = "not loading", # 未加载
	ON_SHOW = "on show" # 显示
	ON_HIDE = "on hide" # 隐藏
	ON_CACHE = "on cache pool" # 处于缓存池中
	NONE = "no state" #无状态
}

win_state = {
	NormalWindow = "normal window", # 显示的时候会直接叠加在上一层
	FullWindow = "full window", # 显示时会把其他所有窗口都隐藏，当隐藏返回时会恢复原先的状态
	PopWindow = "pop window" # 该窗口会显示在最上层
	EMPTY = "empty window" # 未标记的窗口
}


class Window(object):
	"""docstring for Window"""

	name = "" # 我们用该字段标识唯一的页面
	show_state = state.NONE
	win_state = win_state.EMPTY

	def __init__(self, name):
		super(Window, self).__init__()
		self.name = name
		self.show_state = state.NOT_LODING
		self.win_state = NormalWindow

	def show(self):
		print("window on show")
		self.show_state = state.ON_SHOW
		self.win_state = win_state.PopWindow

	def hide(self):
		print("window on hide")
		self.show_state = state.ON_HIDE
		self.win_state = win_state.NormalWindow

	def destory(self):
		print("I am gone")
		self.show_state = state.NOT_LODING
		self.win_state = state.NormalWindow



class ViewController(object):
	"""docstring for ViewController"""

	M = 100 # 缓存池容量
	caches = [] # 用于管理关闭了的窗口
	views = [] # 用于管理当前的页面层级

	def __init__(self, arg):
		super(ViewController, self).__init__()
		self.arg = arg

	def create_view(self, name):
		win = Window(name)
		self.views.append(win)
		
	def show_view(self, name):
		win = self.find_window(name)
		if win != None:
			if win.show_state == state.ON_SHOW:
				print("Invaild operation")
				return
			else if win.show_state == state.ON_HIDE:
				if win in self.views:
					index = self.views.index(win) # 返回在当前页面层级中的索引
					if index == len(self.views-1):
						# 这个页面不可能是最后一个，是就是别的地方有问题了
						print("Invaild operation")
						return
					# 销毁在其上的所有页面
					shouldDestoryViews = self.views[index+1:]
					# 这里如果要求有顺序 可以用索引进行循环，这里未采用这种形式
					for view in shouldDestoryViews:
						self.close_view(view.name)

				else if win in self.caches:
					# 从缓存中取出
					print("LoadFromPool")
					self.caches.pop(win)
					self.views[len(self.views)] = win

				win.show()
		else:
			print("NULL")

	def close_view(self, name):
		cur_size = len(caches)
		win = self.find_window(name)
		if win.win_state != win_state.PopWindow:
			# 不是最顶层为无效操作
			print("Invaild operation")
			return
		if win.show_state != state.ON_SHOW:
			# 隐藏的页面无法关闭
			print("Invaild operation")
			return
		if cur_size < M && win not in caches:
			win.hide()
			self.caches.append(win)
		if cur_size >= M:

			self.destory()

	def close_all_windows(self):
		for view in self.views:
			self.close_view(view.name)

	# 完成check操作
	def check_window(self, name):
		win = self.find_window(name)
		if win != None:
			if win.show_state == state.ON_SHOW:
				return True
		
		return False

	# 根据name标识查找win对象
	def find_window(self, name):
		win = None
		for w in self.views:
			if w.name == name:
				win = w

		if win == None:
			for w in self.caches:
				if w.name == name:
					win = w



