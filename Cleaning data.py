import re # importing the regex module

textfile=open("trialpiece.txt", "rt") # opening the batchfile test and saving it to variable
scannedtext=""
for ll in textfile:
    scannedtext+=ll.rstrip() # stripping the text of new lines

strippedtext=scannedtext.replace("   ", " ") # removing the newlines to help with regex pattern

textfile.close()
#print(strippedtext)

# creating a regex pattern to find only abstract text
#compiling a regex pattern
rgxpat=re.compile(r"Abstract = {(.+?)}")
# finding all the abstract text
list_of_abstracts=rgxpat.findall(strippedtext)
#print(list_of_abstracts) #printing the abstract text (in list form)


# breaking down the abstract into list of words
Frequencylist={}
for each_abstract in list_of_abstracts:
    listofwords=each_abstract.split()
    listofuppercasewords=[]
    for lowerword in listofwords:
        listofuppercasewords.append(lowerword.upper())
    setofwords=set(listofuppercasewords)

    # for every word in that abstract
    for word in setofwords:
        if word in Frequencylist:
            Frequencylist[word]+=1
        else:
            Frequencylist[word]=1

print(Frequencylist)

tableheaders=['Word' , 'Number of Occurances']

print(f"{tableheaders[0]: <15}{tableheaders[1]}")

for key,value in Frequencylist.items():
    print(f"|{key: <15}|{value: <5}|")


