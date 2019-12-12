import random 
import sys 

def stripWordPunctuation(word):
    return word.strip("#^%$@&.,()<>\"\\'~?!;*:[]-+/&—\n` ")

def get_all_words(path='text-file.txt'):
    #the new list we are going to add the stripped word to
    new_text = []

    #open and read file and split the words 
    with open(path, 'r') as file:
        file_text = file.read().split()
    
    #strip each word and append it to new list 
    for line in file_text:
        line = (stripWordPunctuation(line))
        line = line.lower()
        new_text.append(line)

    file.close()

    return new_text

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

        #count down to exit while loop
        num_words -= 1
    
    #print(sentence)
    return sentence


if __name__ == "__main__":
    #get user input 
    input = sys.argv[1:]
    num_words = input[0]
    
    print(get_random_words(int(num_words)))

    