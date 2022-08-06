import random
small = int(input("請輸入最小數字: "))
big = int(input("請輸入最大數字: "))
r = random.randint(small,big)
sum = 0

while True:
	a = input("請輸入數字: ")
	a = int(a)
	if a == r:
		print("終於猜對了")
		break
	elif a > r:
		print("在小一點")
	elif a < r:
		print("在大一點")
	sum+=1
	print("目前猜了", sum, "次")

	

