import os, json, string,re
from multiprocessing import Pool
# Nltk imports
from nltk.corpus import stopwords, indian
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer


def cleaner(_big_data, lang=None):
    # Global stop words set
    stop_words = set()
    # Adding nltp build in wordset
    stop_words.update(string.punctuation)
    if lang is None:
        stop_words.update(stopwords.words('english'))
        stop_words.update(indian.words('hindi.pos'))
    elif lang is "en":
        stop_words.update(stopwords.words('english'))
    elif lang is "hn":
        stop_words.update(indian.words('hindi.pos'))
    else:
        raise ValueError(
            "Invalid lang type only support en and hn and you provided %s" % lang)
    tokenizer = RegexpTokenizer(r'\w+')
    token = tokenizer.tokenize(_big_data)
    clean_token = filter(lambda token: token not in stop_words, token)
    final_string = " ".join(clean_token)

    return final_string



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

def toJSON(object, _path):
    '''
    @Description: Write a object to a file
    '''
    str_obj = json.dumps(object)
    if not os.path.exists(_path):
        os.makedirs(_path)
    File = open(os.path.join(_path,'out.json'), '+w')
    File.write(str_obj)
    

def en_check(word):
    '''
    @Description returns true if a word is english false if it hindi 
    only works for hindi and english => use charters to diff
    '''
    pattern = r"[a-z]"
    if re.match(pattern, word):
        return True
    else:
        return False
    