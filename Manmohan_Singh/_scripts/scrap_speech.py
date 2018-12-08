#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as bs
import os

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()


speech_index=0
printProgressBar(0, 1401, prefix = 'Progress:', suffix = 'Complete', length = 50)
i=1



def getSpeech(i):
    html = requests.get('https://archivepmo.nic.in/drmanmohansingh/speech-details.php?nodeid='+str(i))
    raw_html = bs(html.text,'html.parser')
    complete_path= getSpeechPath(i)
    with open(complete_path+'.txt','w+') as file:
        content_div =  raw_html.find('div',attrs={'class':'contentInner'})
        file.write(content_div.text)


def getSpeechPath(i):
    return os.getcwd() + '/speech_files/speech_'+str(i)

with open('speech_url.txt', 'r') as file:
    for i in range(1,1401):
        printProgressBar(i + 1, 1401, prefix = 'Progress:', suffix = 'Complete', length = 50)
        getSpeech(i)
