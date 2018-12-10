#!/usr/bin/env python3
'''
@Author : Suraj negi
@Description : Tagging / seprating hindi and english data
@Usages: tagger.py [Target Root folder] [ Destination folder ]
@TODO:
  - Fetch files from local storage
  - Seprate English chars
'''
import sys, os
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist


def loadtext(_path):
    '''
    @Description : Get file from destination
                   read and return a list with data
    '''

    stop_words = set(stopwords.words('english'))
    punctuation = [',','.','/','<','>','?',';',':','[',']','{','}','`','~','!','@','#','$','%','^','&','*','(',')','-','_','+','=']
    for p in punctuation:
        stop_words.add(p)

    word_list=[]
    for f in os.listdir(_path):
        file_path = os.path.join(_path,f)
        file = open(file_path)
        file_data = file.read().lower()
        word_list = word_list + word_tokenize(file_data)
        print(f)

    print(len(word_list))
    filter_word=[]
    for w in word_list:
        if w not in stop_words:
            filter_word.append(w)

    fdist=  FreqDist(filter_word)
    top_ten = fdist.most_common(10)
    print(top_ten)

    # for i,j in enumerate(fdist):
    #    if i == 10:
     #       break
      #  print(j,fdist[j])


# program Execution starts here
if __name__ == "__main__":
    # Checking if the the input is valid else exiting
    if len(sys.argv) != 3:
        print("Input Error Please check your input arguments !")
        sys.exit()
    root_path = os.path.abspath(sys.argv[1])
    dest_path = os.path.abspath(sys.argv[2])

    # load text for processing
    loadtext(root_path)
