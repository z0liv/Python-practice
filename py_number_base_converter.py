def number_base_converter(number: str, from_base: int, to_base: int) -> str:
	digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	result = ""
	decimal = 0

	if from_base < 2 or from_base > 36:
		return "ERROR"
	if to_base < 2 or to_base > 36:
		return "ERROR"
	if not number:
		return "ERROR"

	for char in number:
		digit = digits.find(char)

		if digit == -1 or digit >= from_base:
			return "ERROR"
		decimal = decimal * from_base + digit

	if decimal == 0:
		return "0"

	while decimal > 0:
		remainder = decimal % to_base
		result = digits[remainder] + result
		decimal = decimal // to_base
	
	return result


if __name__ == "__main__":
	print(number_base_converter("1010", 2, 10))  # Expected: "10"
	print(number_base_converter("FF", 16, 10))  # Expected: "255"
	print(number_base_converter("255", 10, 16))  # Expected: "FF"
	print(number_base_converter("123", 10, 2))  # Expected: "1111011"
	print(number_base_converter("Z", 36, 10))  # Expected: "35"
	print(number_base_converter("35", 10, 36))  # Expected: "Z"
	print(number_base_converter("123", 1, 10))  # Expected: "ERROR"
	print(number_base_converter("G", 16, 10))  # Expected: "ERROR"
