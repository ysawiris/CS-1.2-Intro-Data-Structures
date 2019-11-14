import sys 

def reverse_sentence(input_sentence):
    new_sentence = ""

    for i in range(len(input_sentence)):
        new_sentence += input_sentence[len(input_sentence) - 1 - i] + " "
    
    return new_sentence

if __name__ == "__main__":
    input = sys.argv[1:]
    print(reverse_sentence(input))
