""" def string_permutation_checker(s1: str, s2: str) -> bool:
	counter_01 = 0
	if len(s1) == 0 and len(s2) == 0:
		return True
	if ((len(s1) != 0 and len(s2) == 0)
		or
		(len(s1) == 0 and len(s2) != 0)):
		return False
	while counter_01 < len(s1) - 1:
		if s1[counter_01] in s2:
			counter_01 += 1
		else:
			return False
	
	return True """
def string_permutation_checker(s1: str, s2: str) -> bool:
	copy_01 = s1.replace(" ", "")
	copy_02 = s2.replace(" ", "")

	if sorted(copy_01) == sorted(copy_02):
		return True
	else:
		return False

if __name__ == "__main__":
	print(string_permutation_checker("abc", "bca"), "# Expected: True")  # Expected: True
	print(string_permutation_checker("abc", "def"), "# Expected: False")  # Expected: False
	print(string_permutation_checker("listen", "silent"), "# Expected: True")  # Expected: True
	print(string_permutation_checker("hello", "bello"), "# Expected: False")  # Expected: False
	print(string_permutation_checker("", ""), "# Expected: True")  # Expected: True
	print(string_permutation_checker("a", ""), "# Expected: False")  # Expected: False
	print(string_permutation_checker("Abc", "abc"), "# Expected: False")  # Expected: False
	print(string_permutation_checker("a gentleman","elegant man"), "# Expected: True")  # Expected: True
