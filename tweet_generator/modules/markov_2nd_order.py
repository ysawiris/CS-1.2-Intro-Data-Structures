from dictogram import Dictogram
from frequency import histogram_dictionary, open_file
import random



class MarkovChain(dict):
    def __init__(self, word_list=None):
        #intialize the super class
        super(MarkovChain, self).__init__()
        
        #if word list is passed, create a markov chain 
        if word_list is not None:
            self.create_markov(word_list)
            self['start'] = Dictogram(['love'])
            self['end'] = Dictogram([''])
    
    def get_text(self, path = 'lyrcis.txt'):
        text = open_file(path)
    
        return text 
    
    def create_markov(self, word_list): 
        
        num_words = len(word_list)  
        
        for index, key1 in enumerate(word_list): 
            if num_words > index + 2:
                key2 = word_list[index + 1]
                word = word_list[index + 2]

                if (key1, key2) not in self:
                    self[(key1, key2)] = Dictogram([word])
                else:
                    self[(key1, key2)].add_count(word)


    def sentence(self, word_list, num_words):



        random_index = random.randint(0, len(word_list) - 1)
        key = (word_list[random_index], word_list[random_index + 1])

        sentence = key[0] + ' ' + key[1]

        for _ in range(num_words):
            word = self[key].sample()

            sentence += " " + word
        
        return sentence
            




    
        

    

        
        
    




if __name__ == "__main__":
    word_list = MarkovChain.get_text("lyrcis.txt")
    markov_chain = MarkovChain(word_list)





    print(markov_chain)

    print(markov_chain.sentence(word_list, 10))

 