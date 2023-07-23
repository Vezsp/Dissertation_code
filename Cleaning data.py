import re #importing the regex module

textfile=open("trialpiece.txt", "rt") # opening the batchfile test and saving it to variable
scannedtext=""
for ll in textfile:
    scannedtext+=ll.rstrip() #stripping the text of new lines

strippedtext=scannedtext.replace("   ", " ") # removing the newlines to help with regex pattern

textfile.close()



#print(strippedtext)

rgxpat=re.compile(r"Abstract = {(.+?)}") #creating a regex pattern to find only abstract text
absonly=rgxpat.findall(strippedtext) #finding all the abstract text
#print(absonly) #printing the abstract text (in list form)

# breaking down the abstract into list of words
brokendownabs=[]
for abstractwhole in absonly:
    listofwords=abstractwhole.split()
    brokendownabs.append(listofwords)
#print(brokendownabs)

#converting all words to uppercase
brokendownabsupper=[]
for abstractsplit in brokendownabs:
    for word in abstractsplit:
        upperword=word.upper()
        brokendownabsupper.append(upperword)
#print(brokendownabsupper)




