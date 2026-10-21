def pattern_tracker(text: str) -> int:
	pattern = 0
	counter = 0

	while counter < len(text) - 1:
		if text[counter].isdigit() and text[counter + 1].isdigit():
			if int(text[counter]) == int(text[counter + 1]) - 1:
				pattern += 1
		counter += 1
	return pattern

if __name__ == "__main__":
	print(pattern_tracker("123"))  # Expected: 2
	print(pattern_tracker("12a34"))  # Expected: 2
	print(pattern_tracker("987654321"))  # Expected: 0
	print(pattern_tracker("01234567"))  # Expected: 7
	print(pattern_tracker("abc"))  # Expected: 0
	print(pattern_tracker("1a2b3c4"))  # Expected: 0
	print(pattern_tracker("112233"))  # Expected: 2
