import random

r = random.randint(0, 100)
count = 0
while True:
	count += 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜中了')
		is_again = input('再玩一次?: ')
		if is_again == "是":
			r = random.randint(0, 100)
			count = 0
			continue
		elif is_again == "否":
			break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第%s次' % count)