#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as BS

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


link_set = set()


BASE_URL =  'https://archivepmo.nic.in/drmanmohansingh/'

printProgressBar(0, 1401, prefix = 'Progress:', suffix = 'Complete', length = 50)
i=1

with open('speech_url.txt','w+') as file:
    for i in range(1401):
        raw_req = requests.get('https://archivepmo.nic.in/drmanmohansingh/speech-all.php?pageid=' + str(i))
        raw_html = BS(raw_req.text,'html.parser')
        printProgressBar(i + 1, 1401, prefix = 'Progress:', suffix = 'Complete', length = 50)
        link_ul = raw_html.find('div',attrs={'class':'speechPan'}).find('ul')
        for li in link_ul.find_all('li'):
            link = li.find('a')
            file.write(BASE_URL + link.get('href')+'\n')




# with open("speech_url.txt","w+") as file:
  #  for link in link_set:
   #     file.write(link+'\n')




