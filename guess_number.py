import random

def generate_answer():
	start = input('請決定隨機數字範圍開始值: ')
	end = input('請決定隨機數字範圍結束值: ')
	start = int(start)
	end = int(end)

	r = random.randint(start, end)
	return r
r = generate_answer()
count = 0
while True:
	count += 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜中了')
		is_again = input('再玩一次?: ')
		if is_again == "Y":
			generate_answer()
			count = 0
			continue
		elif is_again == "N":
			break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第%s次' % count)