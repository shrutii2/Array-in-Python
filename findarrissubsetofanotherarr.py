# # T(N)=O(m*n)          S(N)=O(1)


def isSubset(a, arr2, m, n):
	i = 0
	j = 0
	for i in range(n):
		for j in range(m):
			if(arr2[i] == a[j]):
				break
		if (j == m):
			return 0
	return 1

# Driver code
if __name__ == "__main__":
	
	a = [11, 1, 13, 21, 3, 7]
	arr2 = [11, 3, 7, 1]

	m = len(a)
	n = len(arr2)

	if(isSubset(a, arr2, m, n)):
		print("arr2[] is subset of a[] ")
	else:
		print("arr2[] is not a subset of a[]")

