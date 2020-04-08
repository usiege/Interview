# 17 打印从1到最大的n位数

numbers = "0"
def print_to_maxn_digits(n):
	if n <= 0: 
		return

	while not to_end(numbers):
		print(numbers)

		
def to_end(numbers):
	isOverflow = False
	nTakeOver = 0
	n = len(numbers)
	for i in xrange(n-1,0,-1):
		nSum = int(numbers[i]) + nTakeOver
		if i == n - 1:
			nSum += 1
		if nSum >= 10:
			if i == 0:
				isOverflow = True #最高位
			else:
				nSum -= 10
				nTakeOver = 1
				numbers[i] = str(nSum)
		else:
			numbers[i] = str(nSum)
			break

	return isOverflow


# 20 表示数值的字符串
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        valid_all = num+['+', '-', 'e', 'E','.']
        
        # print(valid_all)
        # write code here
        def is_int(sub_s):
            if len(sub_s)==0:
                return False
            # 判断子字符串是否是整数（包括正整数和负整数，以及不具有符号标识的整数）
            if sub_s[0]=='+' or sub_s[0]=='-':
                sub_s=sub_s[1:]
            for elem in sub_s:
                if elem not in num:
                    return False
            return True

        def is_float(sub_s):
            if len(sub_s)==0:
                return False
            #小数点之前的子字符串需要判断是否是整数
            #小数点之后的子字符串需要判断是否是不带有符号的整数
            if len(sub_s.split('.'))!=2:
                return False
            before,after=sub_s.split('.')
            before_logtic=is_int(before)
            if not before_logtic:
                return False
            for s in after:
                if s not in num:
                    return False
            return True

        for c in s:
            # print(valid_all)
            if c not in valid_all:
                return False
        if 'e' in s or 'E' in s:
            out=s.split('e') if 'e' in s else s.split('E')
            if len(out)!=2:
                return False
            else:
                before, after=out[0],out[1]
            logtic=(is_float(before) or is_int(before)) and is_int(after)
            return logtic
        elif '.' in s:
            return is_float(s)
        else:
            return is_int(s)

if __name__=='__main__':
    for s in ["+100","5e2","-123","3.1416","-1E-16"]:
        print(Solution().isNumeric(s))





