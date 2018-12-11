#!/usr/bin/env python3
'''
@Author : Suraj negi
@Description : Tagging / seprating hindi and english data
@Usages: tagger.py [Target Root folder] [ Destination folder ]
@TODO:
    - Adding custome crops for custom word filter
    - Converting data to json format
'''
<<<<<<< HEAD
# from matplotlib import pylab
import sys, os
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
# from nltk import bigrams
import string

def loadtext(_path):
    '''
    @Description : Get file from destination
                   read and return a list with data
    '''

    stop_words = stopwords.words('english') + list(string.punctuation) + ['also','us']
    # punctuation = ['also'',','.','/','<','>','?',';',':','[',']','{','}','`','~','!','@','#','$','%','^','&','*','(',')','-','_','+','=']
   # for p in punctuation:
    #    stop_words.add(p)

    word_list=[]
    for f in os.listdir(_path):
        file_path = os.path.join(_path,f)
        file = open(file_path)
        file_data = file.read().lower()
        word_list = word_list + word_tokenize(file_data)


    print(len(word_list))
    filter_word=[]
    for w in word_list:
        if w not in stop_words:
            filter_word.append(w)
    print(len(filter_word))
   # fdist=  FreqDist(filter_word)
  #  top_ten = fdist.most_common(10)
 #   print(top_ten)
#    fdist.plot(10,cumulative=False)

    # for i,j in enumerate(fdist):
    #    if i == 10:
     #       break
      #  print(j,fdist[j])

=======
import sys
import os
from Util import loadtext, cleaner
>>>>>>> 273c862123c34548a3203438a1e9cad587f6cd7c

# program Execution starts here
if __name__ == "__main__":
    # Checking if the the input is valid else exiting
    if len(sys.argv) != 3:
        print("Input Error Please check your input arguments !")
        sys.exit()
    root_path = os.path.abspath(sys.argv[1])
    dest_path = os.path.abspath(sys.argv[2])

    # load text for processing
    data_list = loadtext(root_path)
    clean_words = cleaner(data_list, lang="en")
