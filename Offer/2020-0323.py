#!/usr/bin/env python

# 二分查找

def binary_search(l, num):
	left = 0
	right = len(l) - 1
	while left <= right:
		mid = (left + right) // 2
		if num < l[mid]:
			right = mid - 1
		elif num > l[mid]:
			left = mid + 1
		else:
			return mid

	return -1

def binary_search(l, left, right, num):
	if left < right:
		return -1

	if num < l[mid]:
		right = mid - 1
	elif num > l[mid]:
		left = mid + 1
	else:
		return mid

	return binary_search(l, left, right, num)

# 快速排序
# arr[] -> 排序数组
# low -> 起始索引
# high -> 结束索引
def partition(arr, low, high):
	j = low - 1
	pivot = arr[high]

	for i in xrange(low,high):
		if arr[i] <= pivot:
			j = j + 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[j+1], arr[high] = arr[high], arr[j+1]

	return j+1

def quick_sort(arr, low, high):
	if low < high:
		p = partition(arr, low, high)

		quick_sort(arr, low, p-1)
		quick_sort(arr, p+1, high)


# 归并排序

def merge_sort(arr):
	if len(arr) < 1:
		return arr

	mid = len(arr) // 2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])

	return merge(left, right)

def merge(left, right):
	res = []
	i, j = 0, 0

	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			i = i + 1
			res.append(left[i])
		else:
			j = j + 1
			res.append(right[j])

	res.append(left[i:])
	res.append(right[j:])

	return res


