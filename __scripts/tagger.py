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


def loadtext(_path):
    '''
    @Description : Get file from destination
                   read and return a list with data
    '''
    data = []
    for f in os.listdir(_path):
        file_path = os.path.join(_path,f)
        reader = open(file_path, 'r')
        for d in reader.read().split(" "):
            data.append(d)
    for a in data:
        print(a)
    print(len(data))



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
