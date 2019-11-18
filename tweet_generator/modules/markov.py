from dictogram import Dictogram
from frequency import histogram_dictionary, open_file
import random

def get_text(path = 'lyrcis.txt'):
    text = open_file(path)
    
    return text 

class MarkovChain(dict):
    def __init__(self, word_list=None):
        #intialize the super class
        super(MarkovChain, self).__init__()
        
        #if word list is passed, create a markov chain 
        if word_list is not None:
            self.create_markov(word_list)
            self['start'] = Dictogram(['nigga'])
            self['end'] = Dictogram([''])
    
    def create_markov(self, word_list):
        for index, word in enumerate(word_list):

            if self.get(word) is None:
                self[word] = Dictogram()
            
            if index + 1 < len(word_list):
                next = word_list[index + 1]
                self.get(word).add_count(next)
    



if __name__ == "__main__":
    word_list = get_text("lyrcis.txt")
    markov_chain = MarkovChain(word_list)

    print(markov_chain)




