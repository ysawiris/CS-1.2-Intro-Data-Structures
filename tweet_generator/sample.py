import sys
import random
from frequency import open_file, histogram_dictionary, histogram_list

def random_word_by_frequency(histogram):
    tokens = 0   #to tally up the values count 
    count = 0    #to tally up count to pick a word 

    #loop over the value for each key and add them up 
    for count in histogram.values():
        tokens += count
    
    #pick a random number between 
    random_index = random.randint(1, tokens) / tokens
    
    #loop throught the dictionary and divide each value by the tokens
    #then add that value to count and compare num the random_index 
    #if num is greater/ equal to random_index, end the loop and return the word 
    for word in histogram:
        num = histogram[word] / tokens
        count += num 
        if count >= random_index:
            return word 


if __name__ == "__main__":
    input_file = sys.argv[1:]
    file = input_file[0]
    text = open_file(file)
    print(random_word_by_frequency(histogram_dictionary(text)))

