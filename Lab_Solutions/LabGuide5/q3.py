from ctypes import sizeof

with open('read1.txt') as f:
    contents = f.read()

def BruteFroceStringMatch(anArray , pattern):
        #print((anArray))
        for i in range(0 , len(anArray)- len(pattern)):
            j = 0

            #print(pattern[j] == anArray[i+j])
            while (j < len(pattern)) and (pattern[j] == anArray[i+j]):
                j = j + 1
                #print(j)
            
            if j == len(pattern):
                return i

        return -1



pattern = input("Enter a search word: ")
patternArray = []
for chars in pattern:
    patternArray.append(chars)

#print(patternArray)
#print(len(patternArray))
index = BruteFroceStringMatch(contents, patternArray)



print("First index of the text is" , index)

 
