import sys
import random

def stripWordPunctuation(word):
    return word.strip("#^%$@&.,()<>\"\\'~?!;*:[]-+/&—\n` ")

def open_file(path):
    #the new list we are going to add the stripped word to
    new_text = []

    #open and read file and split the words 
    with open(path, 'r') as file:
        file_text = file.read().split()
    
    #strip each word and append it to new list 
    for line in file_text:
        line = (stripWordPunctuation(line))
        new_text.append(line)

    file.close()

    return new_text

def histogram_list(file_text):
    #define our histogram 
    histogram = {}
    list = []

    #loop though our file_text and add text to our histogram 
    for text in file_text:
        if text in histogram.keys():
            histogram[text] += 1
        else:
            histogram[text] = 1
    
    #loop and add each key and value to our list 
    for key, value in histogram.items():
        list.append([key, value])

    return list

def histogram_tuples(file_text):
    #define our histogram 
    histogram = {}
    tuples = []

    #loop though our file_text and add text to our histogram 
    for text in file_text:
        if text in histogram.keys():
            histogram[text] += 1
        else:
            histogram[text] = 1
    
    #loop and add each key and value to our tuples 
    for key, value in histogram.items():
        tuples.append((key, value))
    
    return tuples

def histogram_dictionary(file_text):
    #define our histogram 
    histogram = {}

    #loop though our file_text and add text to our histogram 
    for text in file_text:
        if text in histogram.keys():
            histogram[text] += 1
        else:
            histogram[text] = 1
    return histogram

def unique_words(file_text):
    #define our histogram 
    histogram = {}

    #loop though our file_text and add text to our histogram 
    for text in file_text:
        if text in histogram.keys():
            histogram[text] += 1
        else:
            histogram[text] = 1
    
    return histogram




if __name__ == "__main__":
    input_file = sys.argv[1:]
    file = input_file[0]
    text = open_file(file)
    histogram_dictionary(text)
    histogram_list(text)
    histogram_tuples(text)

    print(unique_words(text))
    print(len(unique_words(text)))