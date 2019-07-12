# coding=utf8
import json
import re

def conver_integers(mystr):
    wordList = re.sub("[^\w]", " ", mystr.lower()).split()
    print(wordList)

    with open('E:/Important Code/index.json', 'r') as f:
        array = json.load(f)
        nums = []
        for i in range(len(wordList)):
            value = array.get(wordList[i])
            if value == None:
                continue
            nums.insert(i, int(value) + 3)    
    return nums      
c = conver_integers('This movie is great. Quite slow and confusing script. Though acting is very good, story seems to be dull')
print(c)
