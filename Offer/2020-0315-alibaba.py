# 转换为千分位
def covert(money):
	res = ""
	if money < 0:
		money = -money

	if isinstance(money, int):
		if money < 0:
			res = "-" + res
		return res + convert_int(money)

	if isinstance(money, float):

		f = int(money)
		pad = money - f
		x = convert_int(money)

		if money < 0:
			res = "-" + res

		return res + x + str(pad)[2:]


	if isinstance(money, str):
		res = "{:,}".format(money)

	return res


def convert_int(money):
	res = ""
	while money>=1000:
		b = money % 1000
		if b == 0:
			b = "000"
		elif b>=1 and b<=9:
			b='00'+str(b)
		elif b>=10 and b<=99:
			b='0'+str(b)
		else:
			b=str(b)
		money = money//1000
		res = ',' + b + res
	res = str(money) + res
	return res
	


def i_want_money(houses):
	maxs = []
	indexes = []

	l = len(houses)
	if l == 0:
		indexes = []
		return
	elif l == 1:
		indexes = [0]
		return houses[0]
	else:
		maxs[0] = houses[0]
		maxs[1] = max(houses[0], houses[1])
		bigger = houses[0] > houses[1] and 0 or 1
		
		indexes.append(bigger)
		for x in xrange(2,l-1):
			maxs[x] = max(maxs[x-2]+houses[x], maxs[x-1])
			bigger = maxs[x-2]+houses[x] > maxs[x-1] and x-2 or x-1

			# indexes.append(x)
			indexes.append(bigger)

	return maxs, indexes


str = "123456"
str[0:1]
str = "sksks"
str.replace('k','8')
str.find('he')

strs = str.split(',')
strs = ['2', '234']

