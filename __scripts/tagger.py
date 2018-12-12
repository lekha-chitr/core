#!/usr/bin/env python3
'''
@Author : Suraj negi
@Description : Tagging / seprating hindi and english data
@Usages: tagger.py [Target Root folder] [ Destination folder ]
@TODO:
    - Adding custome crops for custom word filter
    - Converting data to json format
'''

import sys
import os
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import string
from multiprocessing import Pool


def loadtext(_dir_path, limit=None):
    '''
    @Description : Get file from destination
                   Return raw string having data of all files
    '''
    pool = Pool(4)
    file_list = [os.path.join(_dir_path, f) for f in os.listdir(_dir_path)]
    data_pool = pool.map(_reader,  file_list)
    raw_data = ""
    for data in data_pool:
        raw_data += data
    return raw_data


def _reader(_file_path):
    '''
    @Description : Get file from destination
                   Return string in lower case format
    '''
    file = open(_file_path, 'r', encoding="UTF-8")
    return file.read().lower()


def tokenizeWord(raw_data):
    '''
    @Description : Tokenize word using nltk 
                   Return list of words
    '''
    return word_tokenize(raw_data)


def cleanData(word_token):
    '''
    @Description : Remove all stop word and punctuation 
                   Return filtered string 
    '''
    stop_words = stopwords.words(
        'english') + list(string.punctuation) + ['also', 'us', 'must', 'need']
    filter_word = []
    for w in word_token:
        if w not in stop_words:
            filter_word.append(w)

    return filter_word


def mostCommonWord(fitered_data, length):
    '''
    @Description : Take length of most common word
                    Print most common words 

    '''
    fdist = FreqDist(filtered_data)
    mostCommon = fdist.most_common(length)
    print(mostCommon)


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
    word_token = tokenizeWord(raw_data)
    filtered_data = cleanData(word_token)
    print(len(filtered_data))
    mostCommonWord(filtered_data, 10)
