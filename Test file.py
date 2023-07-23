#import maya as maya
import nltk
from nltk.corpus import stopwords
sw_nltk = stopwords.words('english')

#print("hello")
#edited = maya

textfile=open("trialpiece.txt", "rt") # opening the batchfile test and saving it to variable
scannedtext=""
for ll in textfile:
    scannedtext+=ll.rstrip() # stripping the text of new lines

strippedtext=scannedtext.replace("   ", " ") # removing the newlines to help with regex pattern

textfile.close()
#print(strippedtext)

#words = [word for word in strippedtext.split() if word.lower() not in sw_nltk]
#new_text = " ".join(words)
#print(new_text)
#print("Old length: ", len(strippedtext))
#print("New length: ", len(new_text))

print(sw_nltk)
