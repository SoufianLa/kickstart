import sys
import math
import itertools 

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

for c in range(int(input())):
	n = int(input())
	array = list(map(int, input().split()))
	array_diff = list()
	max_array = list()
	array_diff = [t - s for s, t in zip(array, array[1:])]
	for key, group in itertools.groupby(array_diff): 
		max_array.append(len(list(group)))
		#print(str(key) + " :", list(group))
	res = max(max_array) + 1
	print("Case #{}: {}".format(c+1, res))