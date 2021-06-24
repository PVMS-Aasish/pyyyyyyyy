intro =input("what's your name?")
print(intro)
count = 0
wordCount=1
for i in intro : 
    count=count+1
    
    if(i==" "):
        wordCount=wordCount+1
print("number of words: ")
print(wordCount)
print("number of characters: ")
print(count)