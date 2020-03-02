-- 面试题10

function fibonacci_ori( n )
	-- body
	if n == 0 then return 0 end
	if n == 1 then return 1 end
	return fibonacci_ori(n-1) + fibonacci(n-2)
end

function fibonacci( n )
	-- body	
	res = {0, 1}
	if n < 2 then return res[#res] end

	fibOne = 1
	fibTwo = 0
	fibN = 0
	for i=2,n do
		fibN = fibTwo + fibOne

		fibTwo = fibOne
		fibOne = fibN
	end
	return fibN
end

-- 快速排序

require "math"

function RandomInRange( startNum, endNum )
	-- return a random in startNum~endNum
	math.randomseed(os.time())
	return math.random(startNum, endNum)
end


function partition( data, startNum, endNum )
	if data == nil then return end
	length = #data
	if startNum < 1 or endNum > length then return end

	index = RandomInRange(startNum, endNum)
	data[index], data[endNum] = data[endNum], data[index]

	small = startNum - 1
	for index=startNum,endNum do
		if data[index] < data[endNum] then
			small = small + 1
			if index ~= small then 
				data[small], data[index] = data[index], data[small]
			end
		end
	end
	small = small + 1
	data[small], data[endNum] = data[endNum], data[small]

	return small
end


function QuickSort( data, startNum, endNum )
	if startNum == endNum then return end

	index = partition(data, startNum, endNum)
	if index > startNum then
		QuickSort(data, startNum, index-1)
	end
	if index < endNum then
		QuickSort(data, endNum, index+1)
	end
end

function SortAges( ages )
	if ages == nil then return end

	oldest_age = 99
	times_of_age = {}

	for i=1,oldest_age do
		times_of_age[i] = 0
	end

	length = #ages

	for i=1,length do
		age = ages[i]
		if age < 0 or age > oldest_age then
			-- give a exception
		end

		times_of_age[age] = times_of_age[age]+1
	end

	-- 某个年龄出现了几次，就在数组里设置几次该年龄
	-- 相当于给数组排序，这在处理具有相同数字的数组中非常有用
	index = 1
	for i=1,oldest_age do
		for j=1,times_of_age[i] do
			ages[index] = i
			index = index + 1
		end
	end

end


