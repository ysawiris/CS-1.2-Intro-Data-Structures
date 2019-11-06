import sys
import random
from modules import frequency

def random_word_by_freq(histogram):
    tokens = 0   #to tally up the values count 
    count = 0    #to tally up count to pick a word 
    
    #loop over the value for each key and add them up 
    for count in histogram.values():
        tokens += count
    
    #pick a random number between 
    random_index = random.randint(1, tokens) 
    
    
    #loop throught the dictionary and divide each value by the tokens
    #then add that value to count and compare num the random_index 
    #if num is greater/ equal to random_index, end the loop and return the word 
    for word in histogram:
        num = histogram[word]
        count += num 
        if count > random_index:
            return word 

def test_random_word_by_frequency(text_file):
    words = []
    histogram ={}
    
    #run random_word_by_frequency 100 times and add results to a words list 
    for _ in range(0,100):
        words.append(random_word_by_freq(frequency.histogram_dictionary(text_file)))
    
    #convert our list to a histogram to see our results easier 
    for text in words:
        if text in histogram.keys():
            histogram[text] += 1
        else:
            histogram[text] = 1
    
    print(histogram)

def run_sample_by_freq():

    path = '/Users/ysawiris/dev/CS-1.2-Intro-Data-Structures/tweet_generator/database/lyrcis.txt'
    text = frequency.open_file(path)
    histogram = frequency.histogram_dictionary(text)

    words = []
    sentence = ""
    num_words = 10

    for _ in range(0,10):
        words.append(random_word_by_freq(histogram))
    
    while num_words > 0:
        #Get random number of index
        random_index = random.randint(0, len(words)-1)

        #Get num_word of random word
        random_words = words[random_index]

        #put the words into a sentence 
        sentence += random_words + " "
        
        # Remove word from list of words
        words.remove(random_words)

        #count down to exit while loop
        num_words -= 1
    
    print(sentence)
    return sentence


if __name__ == "__main__":
    run_sample_by_freq()


    



    
    
