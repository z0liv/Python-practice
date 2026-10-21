def cryptic_sorter(strings: list[str]) -> list[str]:
	counter = 0
	tmp = ""
	sort = True

	if len(strings) == 0:
		return ([])
	while sort and len(strings) > 1:
		while counter < len(strings) - 1:
			sort = False
			if (len(strings[counter]) > len(strings[counter + 1])):
				tmp = strings[counter]
				strings[counter] = strings[counter + 1]
				strings[counter + 1] = tmp
				sort = True
				counter = 0
			elif (len(strings[counter]) == len(strings[counter + 1])):
				if (
					strings[counter][0] > strings[counter + 1][0]
				    and not
				    strings[counter][0].capitalize() == strings[counter + 1][0].capitalize()
					):
					tmp = strings[counter]
					strings[counter] = strings[counter + 1]
					strings[counter + 1] = tmp
					sort = True
					counter = 0
				else:
					counter += 1
			else:
				counter += 1
	return strings

if __name__ == "__main__":
	print(cryptic_sorter(["apple","cat","banana","dog","elephant"]))  # Expected: ["cat","dog","apple","banana","elephant"]
	print(cryptic_sorter(["aaa","bbb","AAA","BBB"]))  # Expected: ["aaa", "AAA", "bbb", "BBB"]
	print(cryptic_sorter(["hello","world","hi","test"]))  # Expected: ["hi","test","hello","world"]
	print(cryptic_sorter([]))  # Expected: []
	print(cryptic_sorter([""]))  # Expected: [""]
	print(cryptic_sorter(["pear", "fig", "kiwi", "plum"]))
	print(cryptic_sorter(["Bee", "ant", "bee", "Ant"]))
