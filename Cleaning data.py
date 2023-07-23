import re # importing the regex module

textfile=open("trialpiece.txt", "rt") # opening the batchfile test and saving it to variable
scannedtext=""
for ll in textfile:
    scannedtext+=ll.rstrip() # stripping the text of new lines

strippedtext=scannedtext.replace("   ", " ") # removing the newlines to help with regex pattern

textfile.close()
#print(strippedtext)

# creating a regex pattern to find only abstract text
rgxpat=re.compile(r"Abstract = {(.+?)}") #compiling a regex pattern
list_of_abstracts=rgxpat.findall(strippedtext) # finding all the abstract text
#print(list_of_paragraphs) #printing the abstract text (in list form)








# breaking down the abstract into list of words
Frequencytable={}
for each_abstract in list_of_abstracts:
    listofwords=each_abstract.split()
    for word in listofwords:  # for every word in that abstract
        upperword=word.upper() # make it uppercase. This will help with the dictionary aspect later
        if upperword in Frequencytable:
            Frequencytable[upperword]+=1
        else:
            Frequencytable[upperword]=1

print(Frequencytable)




