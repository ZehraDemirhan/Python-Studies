def StringMatch(text, pattern):
    for i in range(0,len(text) - len(pattern)):
        j = 0
        while j < len(pattern) and pattern[j] == text[i+j]:
            j = j + 1

        if j == len(pattern):
            return i

        return -1

f = open("shark.txt", "r")
print(f.read())
