-- 1-5

-- 由于第一题是赋值运算符重写，Lua没有对符号的定义，所以本题使用C++写法
-- Lua可以使用元表定义.__eq行为，这个属于高级用法，暂放；
--[[
见cpp文件
上述当内存分配不足时，即考虑有可能m_pData为空指针的情况；
]]


-- 2 实现单例
Singleton = {}

function Singleton:new( o )
	o = o or {}
	setmetatable(o, self)
	self.__index = self
	return o
end

function Singleton:Instence(  )
	if self.instence == nil then
		self.instence = self.new()
	end
	return self.instence
end

-- setmetatable
-- __index

-- 3 数组中重复的数字
-- 数组中的数介于0-n-1之间
-- 找出数组中任意一个重复数字
print("3-1")
input = {2, 3, 1, 0, 2, 5, 3}

function duplicate( numbers )
	-- body
	if numbers == nil then
		return nil
	end

	n = #numbers

	for i=1,n do
		if numbers[i] < 0 or numbers[i] > n-1 then
			return nil
		end
	end

	for i=1,n do
		while numbers[i] ~= i-1 do
			if numbers[i] == numbers[numbers[i]+1] then
				return numbers[i]
			end
			numbers[i], numbers[numbers[i]+1] = numbers[numbers[i]+1], numbers[i]
		end
	end
end
print(duplicate(input))

-- 不修改数组找出重复数字
-- 长度为n+1 所有数字都是1~n范围内
-- 同样找出任意一个重复数字
print("3-2")
input = {2, 3, 5, 4, 3, 2, 6, 7}

function getDuplication( numbers )
	if numbers == nil then
		return nil
	end
	first, last = 1, #numbers-1
	while last >= first do
		middle = (last-first) / 2 + first
		count = countRange(numbers, first, middle)

		if last == first then
			if count > 1 then return first
			else break end
		end

		if count > middle-first+1 then
			last = middle
		else
			first = middle+1
		end

	end
	print("end")
	return nil
end

function countRange( numbers, first, last )
	if numbers == nil then
		return 0
	end

	count = 0
	for i=1,#numbers do
		if numbers[i] >= first and numbers[i] <= last then
			count = count + 1;
		end
	end
	return count
end

print(getDuplication(input))

-- 4 二维数组中的查找
-- 从左到右递增
-- 从上到下递增
inputs = {1, 2, 8,  9,
		  2, 4, 9,  12, 
		  4, 7, 10, 13,
		  6, 8, 11, 15}
findme = 10

function find( array, tag, rows, columns )
	found = false
	if array ~= nil and rows > 0 and columns > 0 then
		row = 1
		column = columns

		while row <= rows and column >= 1 do
			target = inputs[row*columns + column]
			if target == tag then
				found = true
				break
			elseif target > tag then
				column = column - 1
			else
				row = row + 1
			end
		end
	end
	return found
end

print(find(inputs, findme, 4, 4))

-- 5 把字符串每个空格替换成"%20"
input = "We are happy."

function replaceBlank( str )
	-- body
	if str == nil or str == "" then return "" end

	originalLength = #str
	numberOfBlank = 0
	for i=1,originalLength do
		c = string.sub(str,i,i)
		-- print(c)
		if c == " " then
			numberOfBlank = numberOfBlank + 1
		end
	end

	print(numberOfBlank)
	newLength = originalLength + numberOfBlank * 2

	indexOfOriginal = originalLength
	indexOfNew = newLength

	print(indexOfNew, indexOfOriginal)

	res = ""
	while indexOfOriginal >= 1 and indexOfNew >= indexOfOriginal do
		c = string.sub(str,indexOfOriginal,indexOfOriginal)
		if(c == " ") then
			res = "0"..res
			indexOfNew = indexOfNew - 1
			res = "2"..res
			indexOfNew = indexOfNew - 1
			res = "%"..res
			indexOfNew = indexOfNew - 1
		else
			res = c..res
			-- res[indexOfNew] = str[indexOfOriginal]
			indexOfNew = indexOfNew - 1
		end
		indexOfOriginal = indexOfOriginal - 1
	end
	return res
end

print(replaceBlank(input))
