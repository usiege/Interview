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
	for i in xrange(l-2):
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
		while i < l-2 and num[i] == num[i+1]:
			i = i + 1;
		
	return res

# 查找四个数的和
# 已排序 无重复
def four_nums(nums, target):
	l = len(nums)
	res = []
	for i in xrange(l-3):
		for j in xrange(i+1, l-2):
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






