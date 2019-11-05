import random 
import sys 

def get_all_words():
    #Open and read in the words in  file
    f = open('/Users/ysawiris/dev/CS-1.2-Intro-Data-Structures/tweet_generator/database/lyrcis.txt', 'r')
    words = f.readlines()
    f.close()
    
    words_list = []

    #Loop over each word and strip the word before adding the a new list 
    for word in words:
        words_list.append(word.strip())
    print(words_list)
    return words_list

def get_random_words(num_words):
    list_of_words = get_all_words()
    sentence = " "

    while num_words > 0:
        #Get random number of index
        random_index = random.randint(0, len(list_of_words)-1)

        #Get num_word of random word
        random_words = list_of_words[random_index]

        #put the words into a sentence 
        sentence += random_words + " "
        
        # Remove word from list of words
        list_of_words.remove(random_words)

        #count down to exit while loop
        num_words -= 1
    
    #print(sentence)
    return sentence


if __name__ == "__main__":
    #get user input 
    input = sys.argv[1:]
    num_words = input[0]
    
    print(get_random_words(int(num_words)))

    