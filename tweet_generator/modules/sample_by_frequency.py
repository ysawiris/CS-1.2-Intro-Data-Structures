import sys
import random
#error will occur when running app in terminal, this line of code is need for Heroku
from modules import frequency
#uncomment the line below to have it work correctly, make sure to comment out line 4 
#import frequency

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

def test_random_word_by_frequency(text_file='test-file.txt'):
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
    path = '/modules/lyrcis.txt'
    text = frequency.open_file(path)
    histogram = frequency.histogram_dictionary(text)

    words = []
    sentence = ""
    num_words = 10
    
    #loop num_words amount of times and add a random word by frequency to a words list 
    for _ in range(0, num_words):
        words.append(random_word_by_freq(histogram))
    
    #loop through each word in words list and add the word to the sentence string 
    for word in words:
        sentence += word + " "

    return sentence


if __name__ == "__main__":
    print(run_sample_by_freq())


    



    
    
