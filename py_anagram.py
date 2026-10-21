def anagram(s1: str, s2: str) -> bool:

	copy_01 = s1.replace(" ", "").lower()
	copy_02 = s2.replace(" ", "").lower()

	if sorted(copy_01) == sorted(copy_02):
		return True
	else:
		return False

""" 
	counter_01 = 0
	if len(copy_01) != len(copy_02):
		return False
	while counter_01 < len(s1) - 1:
		if s1[counter_01].upper() in s2.upper():
			counter_01 += 1
		else:
			return False
	
	return True """


if __name__ == "__main__":
	print(anagram("listen", "silent"))  # Expected: True
	print(anagram("Triangle", "Integral"))  # Expected: True
	print(anagram("Dormitory", "Dirty Room"))  # Expected: True
	print(anagram("hello", "world"))  # Expected: False
	print(anagram("", ""))  # Expected: True
	print(anagram("abc", "abcc"))  # Expected: False
