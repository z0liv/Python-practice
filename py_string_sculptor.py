def string_sculptor(text: str) -> str:
	result = ""
	counter = 0
	lower = True
	while counter < len(text):
		if text[counter].isalpha():
			if lower:
				result += text[counter].lower()
				lower = False
			else:
				result += text[counter].upper()
				lower = True
		else:
			result += text[counter]
		counter += 1

	return result




if __name__ == "__main__":
	print(string_sculptor("hello"))  # Expected: "hElLo"
	print(string_sculptor("Hello World"))  # Expected: "hElLo WoRlD"
	print(string_sculptor("   hello   "))  # Expected: "   hElLo   "
	print(string_sculptor("abc123def"))  # Expected: "aBc123DeF"
	print(string_sculptor("Python3.9!"))  # Expected: "pYtHoN3.9!"
	print(string_sculptor(""))  # Expected: ""
