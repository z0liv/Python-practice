def	twist_sequence(arr: list[int], k: int) -> list[int]:
	result = []
	counter = 0
	if k == 0 or len(arr) == 0:
		return arr
	if k > len(arr):
		k = k % k
	for n in arr[k + 1:]:
		result.append(n)
	while counter < k + 1:
		result.append(arr[counter])
		counter += 1
	return result


if __name__ == "__main__":
	print(twist_sequence([1,2,3,4,5], 2))  # Expected: [4,5,1,2,3]
	print(twist_sequence([1,2,3], 1))  # Expected: [3,1,2]
	print(twist_sequence([1,2,3,4], 0))  # Expected: [1,2,3,4]
	print(twist_sequence([1,2,3], 5))  # Expected: [2,3,1]
	print(twist_sequence([], 3))  # Expected: []
