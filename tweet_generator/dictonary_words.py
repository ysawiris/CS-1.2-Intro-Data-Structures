from random import choice
import sys 

def get_random_words():
    ''' Open and read in the words file'''
    f = open('/usr/share/dict/words', 'r')

    words = f.readlines()

    f.close()

    for word in words:
        word_list = word.split('\n')

    print (word_list)

    

    '''select a random set of words from the file and store in a data type'''

get_random_words()