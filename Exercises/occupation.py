import pandas as pd
import numpy as np
import urllib.request
import csv
import re

def step1():
    with urllib.request.urlopen('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user') as f:
        bytes_download = f.read().decode('utf-8').splitlines()
    
    # data/set = bytes_download.replace('|',',')
    # print(dataset)

    with open('Data/occupation.txt', 'w') as file:
        file.writelines("\n".join(bytes_download))

    

    with open('Data/occupation.csv', 'w') as filecsv:
        with open('Data/occupation.txt', 'r') as file:
            writer= csv.writer(filecsv, delimiter=',')
            for line in file:
                writer.writerow(line.strip().split('|'))


       
    print('Dataset is saved inside Data directory as occupation.csv')
step1()