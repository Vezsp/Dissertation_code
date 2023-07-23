import re # importing the regex module
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
sw_nltk = stopwords.words('english')

# opening the batchfile test and saving it to variable. Removing newlines and extra spaces
textfile=open("Test batch file.txt", "rt", encoding="utf8")
scannedtext=textfile.read()
strippedtext=scannedtext.replace("   ", " ")
strippedtext=strippedtext.replace("\n", "")
textfile.close()
print("Textfile put into variable 'textfile'.")


# creating a regex pattern to find only abstract text
rgxpat=re.compile(r"Abstract = {(.+?)}")
list_of_abstracts=rgxpat.findall(strippedtext)
print("Number of abstracts: ", len(list_of_abstracts))


# breaking down the abstract into list of words
frequency_dict={}
punc=""".,/"""
for each_abstract in list_of_abstracts:
    listofwords=each_abstract.split()
    list_of_upper_case_words=[]
    for lowerword in listofwords:
        for char in lowerword:
            if char in punc:
                lowerword=lowerword.replace(char,"")
            else:
                continue
        if lowerword.lower() not in sw_nltk:
            list_of_upper_case_words.append(lowerword.upper())
        else:
            continue
    set_of_words=set(list_of_upper_case_words)
#print(set_of_words)
    # for every word in that abstract, add it to the frequency dictionary
    for word in set_of_words:
        if word in frequency_dict:
            frequency_dict[word]+=1
        else:
            frequency_dict[word]=1
#print(frequency_list)


#Creating table
table_headers=['Word' , 'Number of Occurances']
print(f"{table_headers[0]: <15}{table_headers[1]}")
for key,value in frequency_dict.items():
    print(f"|{key: <15}|{value: <5}|")
print("Length of table: ", len(frequency_dict))

#Creating bar graph
words = list(frequency_dict.keys())
No_Of_Occ = list(frequency_dict.values())
plt.bar(words, No_Of_Occ)
plt.title("Number of times word occurs:")
plt.xlabel('Word')
plt.ylabel('No. of times')
plt.show()


