def inter(s1: str, s2: str) -> str:
	result: str = ""
	counter_1 = 0

	while counter_1 < len(s1):
		counter_2 = 0
		while counter_2 < len(s2):
			if s1[counter_1] == s2[counter_2]:
				if s1[counter_1] not in result:
					result += s1[counter_1]
			counter_2 += 1
		counter_1 += 1
	return result

if __name__ == "__main__":
	print(inter("hello", "world"))  # Expected: "lo"
	print(inter("banana", "band"))  # Expected: "ban"
	print(inter("abcabc", "bc"))  # Expected: "bc"
	print(inter("abc", "xyz"))  # Expected: ""
	print(inter("", "abc"))  # Expected: ""
