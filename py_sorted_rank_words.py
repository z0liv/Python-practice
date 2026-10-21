def test_ascii(s1: str, s2: str) -> bool:
    for i in range(len(s1)):
        if s1[i].lower() > s2[i].lower():
            return True
        elif s1[i].lower() < s2[i].lower():
            return False
    return False
        

def sort_ranked_words(words: list[str]) -> list[str]:
    counter = 0
    tmp = ""
    sort = True

    if len(words) == 0:
        return ([])
    while sort and len(words) > 1:
        while counter < len(words) - 1:
            sort = False
            if (len(words[counter]) > len(words[counter + 1])):
                tmp = words[counter]
                words[counter] = words[counter + 1]
                words[counter + 1] = tmp
                sort = True
                counter = 0
            elif (len(words[counter]) == len(words[counter + 1])):
                if (test_ascii(words[counter], words[counter + 1])):
                    tmp = words[counter]
                    words[counter] = words[counter + 1]
                    words[counter + 1] = tmp
                    sort = True
                    counter = 0
                else:
                    counter += 1
            else:
                counter += 1
    return words


if __name__ == "__main__":
    print(sort_ranked_words(["pear", "fig", "kiwi", "plum"]))
    print(sort_ranked_words(["Bee", "ant", "bee", "Ant"]))
    print(sort_ranked_words(["Zoo!", "zap?", "zen.", "zoo!"]))

