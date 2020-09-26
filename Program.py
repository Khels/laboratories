num = int(input())
for i in range(1, num + 1):
	for j in range(i, num):
		print(' ', end='')
	for k in range(1, i + 1):
		print(k, end='')
	for l in range(i - 1, 0, -1):
		print(l, end='')
	print()