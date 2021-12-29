import os
import pickle as pick
#To Use the file add the following to the top of the python file
'''
---------------------------------------
Syspath import snippet
---------------------------------------
import sys
sys.path.append('/home/yhong')


---------------------------------------
Argument Parsing Snippet
---------------------------------------
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True, help="path to images directory")
args = vars(ap.parse_args())
'''

#TODO: Make this into a global module available in pip3 or atelast have a setup.py
def get_file_dir(file):
    '''
    Inputs to this function will be __file__
    '''
    return os.path.dirname(file) +'/'

def traverse_dir_and_do_func(cwd, dirs, func):
    '''
    passes params to func,
    cwd, idx, dir_name
    '''
    for i,d in enumerate(dirs):
        d_path = os.path.join(cwd, d)
        func(cwd=cwd, idx=i, dir_name=d)

def mkdir(dirname):
    try:
        os.mkdir(imgt_save_dir)
    except:
        print(dirname, 'exists')



def writeListToFile(writeList,filename):
    with open(filename, 'w') as f:
        for item in writeList:
            f.write("%s\n" % item)

def writeFileToList(filename):
    returnList = []
    with open(filename, 'r') as filehandle:
        for line in filehandle:
            line = line.rstrip('\n')
            returnList.append(line)
    return returnList

def unpickle(file):
    with open(file, 'rb') as fo:
        data = pick.load(fo, encoding='bytes')
    return data

def pickle(data,filename):
    f = open(filename,"wb")
    pick.dump(data,f,protocol=2)
    f.close()

def printFileByLine(filename):
    f = open(filename, 'r')
    line = f.readline()
    while line:
        line = f.readline()
    f.close()


'''
def fixEncoding(filename):
    with codecs.open(filename, 'r', encoding='iso-8859-15') as f:
        text = f.read()
    # process Unicode text
    with codecs.open(filename, 'w', encoding='utf8') as f:
        f.write(text)
'''

def filesInDir(dir):
    files = os.listdir(dir)
    return files


def printArray(array):
    for a in array:
        print(a)
        print()

import math
import sys
import random as rand
    
