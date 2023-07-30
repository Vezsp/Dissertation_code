import re # importing the regex module
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 8})
import numpy as np
import nltk
from nltk.corpus import stopwords
sw_nltk = stopwords.words('english')
import numpy as np

# opening the batchfile test and saving it to variable. Removing newlines and extra spaces
textfile=open("practice finding articles text.txt", "rt", encoding="utf8")
scannedtext=textfile.read()
strippedtext=scannedtext.replace("   ", " ")
strippedtext=strippedtext.replace("\n", "")
textfile.close()
#print(strippedtext)

rgxarticlepattern=re.compile(r"article\{(.*?),DA ")
list_of_articles=rgxarticlepattern.findall(strippedtext)
print(len(list_of_articles))

# creating a regex pattern to find only the data I need text
rgxabspat=re.compile(r"Abstract = {(.+?)}")
rgxyearpat=re.compile(r"Year = {(.+?)}")
rgxmonthpat=re.compile(r"Month = {(.+?)}")
rgxaddresspat=re.compile(r"Address = {(.+?)}")
rgxtitlepat=re.compile(r"Title = {(.+?)}")
list_of_abstracts=rgxabspat.findall(strippedtext)
list_of_years=rgxyearpat.findall(strippedtext)
list_of_dates=rgxmonthpat.findall(strippedtext)
list_of_addresses=rgxaddresspat.findall(strippedtext)
list_of_titles=rgxtitlepat.findall(strippedtext)

#print("Number of abstracts: ", len(list_of_abstracts))
#print("Number of years: ", len(list_of_years))
#print("Number of dates: ", len(list_of_dates))
#print("Number of Addresses: ", len(list_of_addresses))
#print("Number of Titles: ", len(list_of_titles))



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

#creating dictionary that includes all words appearing over 100 times in all abstracts
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


