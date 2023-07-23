import re # importing the regex module
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
sw_nltk = stopwords.words('english')

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
frequency_list={}
for each_abstract in list_of_abstracts:
    listofwords=each_abstract.split()
    list_of_upper_case_words=[]
    for lowerword in listofwords:
        #if lowerword.lower() not in sw_nltk:
        list_of_upper_case_words.append(lowerword.upper())
        #else:
           # continue
    set_of_words=set(list_of_upper_case_words)

#print(set_of_words)

    # for every word in that abstract
    for word in set_of_words:
        if word in frequency_list:
            frequency_list[word]+=1
        else:
            frequency_list[word]=1

print(frequency_list)

table_headers=['Word' , 'Number of Occurances']

#print(f"{table_headers[0]: <15}{table_headers[1]}")


#for key,value in frequency_list.items():
    #print(f"|{key: <15}|{value: <5}|")

words = list(frequency_list.keys())
No_Of_Occ = list(frequency_list.values())

#plt.bar(words, No_Of_Occ)
#plt.title("Number of times word occurs:")
#plt.xlabel('Word')
#plt.ylabel('No. of times')
#plt.show()


