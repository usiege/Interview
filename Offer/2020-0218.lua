#!/usr/bin/env lua

--9
--用两个栈实现队列

require "tools"

stack1 = Stack
stack2 = Stack

print(stack1)
print(stack2)

function appendTail( element )
	-- body
	stack1.push(element)
end


function deleteHead( ... )
	-- body
	if stack2:size() <= 0 then
		while stack1:size() > 0 do
			data = stack1:top()
			stack1:pop()
			stack2:push(data)
		end
	end
	if stack2:size() == 0 then return end
	head = stack2:top()
	stack2:pop()

	return head
end
