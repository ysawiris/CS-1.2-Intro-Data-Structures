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
    
    def get_text(self, path = 'lyrcis.txt'):
        text = open_file(path)
    
        return text 
    
    def create_markov(self, word_list):
        num_words = len(word_list)

        for index, key in enumerate(word_list):

            if self.get(key) is None:
                self[key] = Dictogram()
            
            if num_words > index + 1:
                word = word_list[index + 1]
                self.get(key).add_count(word)
    
    def generate_sentence(self, word_list, num_words):
        random_index = random.randint(0, len(word_list) - 1)

        random_word = word_list[random_index]

        word = random.choice(list(self.get(random_word)))

        sentence = word 

        for _ in range(num_words):
            word = self[word].sample()

            sentence += " " + word 
        
        return sentence
    


if __name__ == "__main__":
    word_list = MarkovChain.get_text("lyrcis.txt")
    markov_chain = MarkovChain(word_list)



    print(markov_chain)

    print(markov_chain.generate_sentence(word_list, 10))






