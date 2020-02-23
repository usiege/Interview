#!/usr/bin/env lua
print("tools module")
-- require "class"

-- there is a implement of stack 

local modulename = ...

-- local Stack = class("Stack")
local Stack = {}
modulename.stack = Stack
_G[modulename].stack = Stack

function Stack:init(  )
	-- body
	self.size = 0
	self.table = {}
end

function Stack:size(  )
	-- body
	return self.size or 0
end


function Stack:push( something )
	-- body
	local size = self:size()
	self.table[size+1] = something
	self.size = size + 1
end

function Stack:pop( something )
	-- body
	local size = self:size()
	if size == 0 then return nil end
	self.table[size] = nil
	self.size = size - 1
end

function Stack:top( ... )
	-- body
	if self.size > 0 then
		return self.table[self.size]
	else
		return nil
	end
end

return tools