def countWordsFromFile():
    fileName=input ("enter the file name :- ")
    file=open(fileName,'r')
    noOfWords=0
    for line in file :
        words=line.split()
        noOfWords=noOfWords+len(words)
    print("no. of Words :- ")
    print(noOfWords)

countWordsFromFile()