def hidenp(small: str, big: str) -> bool:
	sm_count = 0
	big_count = 0

	while sm_count < len(small):
		if big_count >= len(big):
			return False
		if small[sm_count] == big[big_count]:
			sm_count += 1
		big_count += 1
	return True

if __name__ == "__main__":
	print(hidenp("abc", "a1b2c3"))  # Expected: True
	print(hidenp("ace", "abcde"))  # Expected: True
	print(hidenp("aec", "abcde"))  # Expected: False
	print(hidenp("", "abc"))  # Expected: True
	print(hidenp("abc", "ab"))  # Expected: False
	print(hidenp("aaaa", "aaa"))  # Expected: False
	print(hidenp("sing","subsequence testing"))  # Expected: True
