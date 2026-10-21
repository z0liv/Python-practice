def bracket_validator(s: str) -> bool:
	opening = ["(", "[", "{"]
	closed = [")", "]", "}"]
	brackets = {"(": ")", "[":"]", "{":"}"}
	stack = []

	for char in s:
		if char in opening:
			stack.append(char)
		elif char in closed:
			bracket = stack.pop()
			if brackets[bracket] != char:
				return False

	if len(stack) == 0:
		return True
	else:
		return False


if __name__ == "__main__":
	print(bracket_validator("()"))  # Expected: True
	print(bracket_validator("hello(world)"))  # Expected: True
	print(bracket_validator("((())"))  # Expected: False
	print(bracket_validator(""))  # Expected: True
	print(bracket_validator("()[]{}"))  # Expected: True
	print(bracket_validator("(]"))  # Expected: False
	print(bracket_validator("([)]"))  # Expected: False
	print(bracket_validator("{[]}"))  # Expected: True
