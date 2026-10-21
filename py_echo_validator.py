def echo_validator(text: str) -> bool:
	start = 0
	end = len(text) - 1

	if len(text) == 0:
		return False
	while start != end:
		if (start > len(text) - 1 or end <= 0):
			return True
		if text[start] == " ":
			start += 1
		if text[end] == " ":
			end -= 1
		if text[start].capitalize() != text[end].capitalize():
			return False
		start += 1
		end -= 1
	return True

if __name__ == "__main__":
	print(echo_validator("racecar"))  # Expected: True
	print(echo_validator("A man a plan a canal Panama"))  # Expected: True
	print(echo_validator("race a car"))  # Expected: False
	print(echo_validator("Was it a car or a cat I saw"))  # Expected: True
	print(echo_validator("hello"))  # Expected: False
	print(echo_validator("Madam Im Adam"))  # Expected: True
	print(echo_validator("madam"))  # Expected: True
	print(echo_validator("Able was I ere I saw Elba"))  # Expected: True
	print(echo_validator(""))  # Expected: False
