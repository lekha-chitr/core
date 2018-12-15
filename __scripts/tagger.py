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
from Util import loadtext, cleaner, toJSON, en_check

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
    clean_words = cleaner(data_list)
    new_words = clean_words.split(" ")
    en = {}
    hn = {}
    for i in new_words:
        if en_check(i):
            if i in en:
                en[i] += 1
            else:
                en[i] = 1
        else:
            if i in hn:
                hn[i] += 1
            else:
                hn[i] = 1

    master = {
        "meta": {
            "total_english": len(en),
            "total_hindi": len(hn)
        },
        "en": en,
        "hn": hn
    }
    toJSON(master, dest_path)
