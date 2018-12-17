import os, json, string,re
from multiprocessing import Pool
# Nltk imports
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize,RegexpTokenizer
from nltk.stem import WordNetLemmatizer




def cleaner(raw_data, lang=None):

    '''
       Description : Methods takes the raw string and remove the stop words according to
                     langugae (Hindi and English Supported) and lemmatize the words to root
                     and  return the list of clean word tokens.

    '''

    # Lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Global stop words list
    stop_words = ['must','us','need','also']
    stop_words+=string.punctuation
    stop_words_hi = stopwords_hindi()

    # Add stop words accroding to language
    if lang is None:
        stop_words+=stopwords.words('english')
        stop_words+=(stop_words_hi)
    elif lang is "en":
        stop_words+=stopwords.words('english')
    elif lang is "hn":
        stop_words+=(stop_words_hi)
    else:
        raise ValueError(
            "Invalid lang type only support en and hn and you provided %s" % lang)


    # Tokenizing the raw data
    tokenizer = RegexpTokenizer(r'\w+')
    token_list = tokenizer.tokenize(raw_data)

    # Removing punctuation and stop words from data
    clean_token=[]
    for token in token_list:
        if token not in stop_words:
            clean_token.append(lemmatizer.lemmatize(token))
    return clean_token





def _reader(_file_path):
    '''
    @Description :
    Read the file and convert it to lower case
    '''
    file = open(_file_path, 'r',encoding="UTF-8")
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
    p = r"[a-z]"

    if re.match(p,word):
        return True
    else:
        return False





def stopwords_hindi():
    '''
       @Description : It returns list of stop words available in hindi from a stop word
                     text file present in Custom File folder
    '''
    with open("Custom_Files/stopwords-hi.txt",encoding="UTF-8") as file:
        return file.read().split('\n')
