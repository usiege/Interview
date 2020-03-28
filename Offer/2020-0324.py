# 两数之和
def two_sum(nums, target):
	dic = {}
	l = len(nums)
	for i in xrange(l):
		dic[i] = nums[i]

	nums = sort_nums(nums)

	res = []
	start, end = 0, l-1
	while start < end:
		total = nums[start] + nums[end]
		if t == target:
			res.append(start)
			res.append(end)
		elif t > target:
			end = end - 1
		else
		 	start = start + 1

	# 最后返回的结果需要从dic中取得
	return res


def sort_nums(nums):
	//快速排序
	return nums


# 三数之和 考虑有重复数的情况
def three_num(nums, target):
	# 排序数组 且 记录排序前的数组顺序
	dic = {}
	l = len(nums)
	for i in xrange(l):
		dic[i] = nums[i]

	nums = sort_nums(nums)

	res = [] #res中保存的是下标
	for i in xrange(l-1):
		start = i + 1
		end = l - 1
		t = nums[i] + nums[start] + nums[end]
		while start < end:
			if t == target:
				save = []
				save.append(i)
				save.append(start)
				save.append(end)
				res.append(save)
				start = start + 1
				end = end - 1
				# 如果有重复数
				while start < end and nums[start] == nums[start+1]:
					start = start + 1
					pass
				while start < end and nums[end] == nums[end-1]:
					end = end - 1
					pass

			elif t > target:
				end = end - 1
			else:
				start = start + 1

		while i < l-1 and num[i] == num[i+1]:
			i = i + 1;
		
	return res

# 查找四个数的和
# 已排序 无重复
def four_nums(nums, target):
	l = len(nums)
	res = []
	for i in xrange(l-2):
		for j in xrange(i+1, l-1):
			start = j + 1
			end = l - 1
			t = nums[i] + nums[j] + nums[start] + nums[end]
			if t == target:
				save = []
				save.append(i)
				save.append(start)
				save.append(end)
				res.append(save)
				start = start + 1
				end = end - 1
			elif t > target:
				end = end - 1
			else:
				start = start + 1

	return res


# 网上解法
def Sum4(arr, target):
    arr.sort()
    len1 = len(arr)
    res = []
    if len1<=3:
        print(res)
 
    for i in range(len1 - 2):
        for j in range(i + 1, len1):
            ss = target - arr[i] - arr[j]
            left, right = j + 1, len1 - 1
            while left<right:
                sum = arr[left] + arr[right]
                if sum == ss and [arr[i], arr[j], arr[left], arr[right]] not in res:
                    res.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                elif sum < ss:
                    left += 1
                else:
                    right -= 1
    print(res)

# 哈希表解法
def Sum4(arr, target):
    res = []
    for i, value1 in enumerate(arr):
        for j, value2 in enumerate(arr[i + 1:]):
            for k, value3 in enumerate(arr[i + 2:]):
                if (target - value1 - value2 - value3) in arr[i+3:]:
                    tmp = [value1, value2, value3 ,target - value1 - value2 - value3]
                    tmp.sort()
                    res.append(tuple(tmp))
    res = list(set(res))

————————————————
版权声明：本文为CSDN博主「GeekZW」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/zichen_ziqi/java/article/details/81417262






