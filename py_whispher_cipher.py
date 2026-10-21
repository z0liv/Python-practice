def whisper_cipher(text: str, shift: int) -> str:
	result = ""
	alpha_min = "abcdefghijklmnopqrstuvwxyz"
	alpha_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	counter = 0
	found: int
	pos: int

	while counter < len(text):
		if text[counter].isalpha():
			if text[counter].islower():
				found = alpha_min.find(text[counter])
				pos = found + shift
				if pos >= 26:
					pos = pos % 26
				result += alpha_min[pos]
			else:
				found = alpha_may.find(text[counter])
				pos = found + shift
				if pos >= 26:
					pos = pos % 26
				result += alpha_may[pos]
		else:
			result += text[counter]
		counter += 1

	return result

if __name__ == "__main__":
	print(whisper_cipher("hello", 3))  # Expected: "khoor"
	print(whisper_cipher("Hello World!", 1))  # Expected: "Ifmmp Xpsme!"
	print(whisper_cipher("xyz", 3))  # Expected: "abc"
	print(whisper_cipher("ABC123def", 5))  # Expected: "FGH123ijk"
	print(whisper_cipher("", 10))  # Expected: ""
	print(whisper_cipher("abc", -3))  # Expected: "xyz"
