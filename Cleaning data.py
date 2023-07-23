import re # importing the regex module
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 8})
import numpy as np
import nltk
from nltk.corpus import stopwords
sw_nltk = stopwords.words('english')
import numpy as np

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

sorted_frequency_dict=sorted(frequency_dict.items(), key=lambda x:x[1], reverse=True)
converted_freq_dict=dict(sorted_frequency_dict)
#print(converted_freq_dict)

edited_freq_dict = dict(filter(lambda pair: pair[1]>= 100, converted_freq_dict.items()))

#Creating table
table_headers=['Word' , 'Number of Occurances']
print(f"{table_headers[0]: <15}{table_headers[1]}")
counter=0
for key,value in edited_freq_dict.items():
        print(f"|{key: <30}|{value: <5}|")
        counter+=1
print("Length of table: ", counter)

#Creating bar graph
words = list(edited_freq_dict.keys())
No_Of_Occ = list(edited_freq_dict.values())
plt.bar(words, No_Of_Occ)
plt.xticks(rotation=75, horizontalalignment="center")
plt.title("Number of times word occurs:")
plt.xlabel('Words', labelpad=20)
plt.ylabel('No. of times')
plt.show()


