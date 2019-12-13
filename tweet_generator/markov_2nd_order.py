from dictogram import Dictogram
from frequency import open_file, dictionary_phodict
import random



class MarkovChain(dict):
    def __init__(self, word_list=None):
        #intialize the super class
        super(MarkovChain, self).__init__()
        
        #if word list is passed, create a markov chain 
        if word_list is not None:
            self.create_markov(word_list)

    
    def get_text(self, path = 'lyrics.txt'):
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
        sentence = ""
        
        random_index = random.randint(0, len(word_list) - 1)
        key = (word_list[random_index], word_list[random_index + 1])

        words = []

        while len(sentence) < num_words:  
            
            word = self[key].sample()

            
            words.append(word)
            sentence += " " + word

            key = (key[1], word)
        
        sentence = " ".join(words)

        return sentence
            




    
        

def run_generator():

    word_list = MarkovChain.get_text("lyrics.txt")
    markov_chain = MarkovChain(word_list)


    lyric_1 = markov_chain.sentence(word_list, 25)
    
    print("Lyric 1: {}".format(lyric_1))

    last_word = get_last_word(lyric_1)

    print("last word: {}".format(last_word))

    last_word_pho = convert_word_to_phodict(last_word)

    print("last word pho: {}".format(last_word_pho))

    while True:    
        lyric_2 = markov_chain.sentence(word_list, 25)

        last_word_2 = get_last_word(lyric_2)

        last_word_pho_2 = convert_word_to_phodict(last_word_2)
        
        print(last_word_pho_2)

        if last_word_pho_2 is None:
            continue

        print("Lyric 1: {}".format(last_word_pho[-2:]))
        print("Lyric 2: {}".format(last_word_pho_2[-2:]))

        if last_word_pho_2[-1:] == last_word_pho[-1:]:
            lyric_1 += " " + lyric_2
            break


    return lyric_1


def get_last_word(lyric):
    list = lyric.split(" ")

    word = list[len(list) - 1]

    return word 



def convert_word_to_phodict(word):

    phodict = dictionary_phodict()

    for key, value in phodict.items():
        if word.upper() == key:
            return value
    
    









        
        
    




if __name__ == "__main__":
    print(run_generator())

 