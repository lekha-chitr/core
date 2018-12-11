import os
from multiprocessing import Pool
# Nltk imports
from nltk.corpus import stopwords, indian
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
import string 

def cleaner(_big_data, lang=None):
    # Global stop words set
    stop_words = set()
    # Adding nltp build in wordset
    stop_words.update(string.punctuation)
    # if lang is None:
    stop_words.update(stopwords.words('english'))
    stop_words.update(indian.words('hindi.pos'))
    # elif lang is "en":
    #     stop_words.update(stopwords.words('english'))
    # elif lang is "hn":
    #     stop_words.update(indian.words('hindi.pos'))
    # else:
    #     raise ValueError("Invalid lang type only support en and hn and you provided %s" % lang)


    tokenizer = RegexpTokenizer(r'\w+')
    token = tokenizer.tokenize(_big_data)
    clean_token = filter(lambda token: token not in stop_words, token)
    final_string = " ".join(clean_token)

    tokenizes_list = word_tokenize(final_string)
    print(len(tokenizes_list))

def _reader(_file_path):
    file = open(_file_path, 'r')
    return file.read().lower()


def loadtext(_dir_path, limit=None):
    '''
    @Description : Get file from destination
                   read and return a list with content of every file in a list
    TODO: change dis
    '''
    pool = Pool(4)
    file_list = [os.path.join(_dir_path, f) for f in os.listdir(_dir_path)]
    data_pool = pool.map(_reader,  file_list)
    single_string = ""
    for string in data_pool:
        single_string += string
    return single_string
