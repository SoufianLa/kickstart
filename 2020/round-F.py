import sys
import math

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

for c in range(int(input())):
	order = list()
	out = list()
	n,x = map(int, input().split())
	money = list(map(int, input().split()))
	for e in range(n):
		order.append([e, math.ceil(money[e]/x)])
	order.sort(key=lambda x:x[1])

	for i in order:
		out.append(i[0]+1)
	print("Case #{}: {}".format(c+1, ' '.join([str(elem) for elem in out])))