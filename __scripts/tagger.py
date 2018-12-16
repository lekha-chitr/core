#!/usr/bin/env python3
'''
@Author : Suraj negi
@Description : Tagging / seprating hindi and english data
@Usages: tagger.py [Target Root folder] [ Destination folder ]
@TODO:
    - Adding custome crops for custom word filter
    - Converting data to json format
'''
# from matplotlib import pylab
import sys
import os

from nltk.probability import FreqDist
from Util import loadtext, cleaner, toJSON, en_check







def mostCommonWord(clean_words, length):
    '''
    @Description : Take length of most common word
                    Print most common words

    '''
    fdist = FreqDist(clean_words)
    mostCommon = fdist.most_common(length)
    return mostCommon








# program Execution starts here
if __name__ == "__main__":
    # Checking if the the input is valid else exiting
    if len(sys.argv) != 3:
        print("Input Error Please check your input arguments !")
        sys.exit()
    root_path = os.path.abspath(sys.argv[1])
    dest_path = os.path.abspath(sys.argv[2])

    # load text for processing
    raw_data = loadtext(root_path)
    clean_words = cleaner(raw_data)

    # compute hind/english words
    en=0
    hn=0
    hn_list=[]
    for word in clean_words:
        if en_check(word):
            en+=1
        else:
            hn+=1
            hn_list.append(word)

    # Saving json data
    master = {
        "meta": {
            "total_english": en,
            "total_hindi": hn
        },
        "en": mostCommonWord(clean_words,20),
        "hn": hn_list
    }
    print(master)
    toJSON(master, dest_path)
    
   # mostCommonWord(clean_words,10)





    
