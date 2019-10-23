import sys
import random

def rearrange_words(input_words):
    new_list = []

    while(len(new_list) < len(input_words)):
        random_index = random.randint(0, len(input_words)-1)
        random_word = input_words[random_index]

        if random_word in new_list:
            continue

        new_list.append(random_word)

    rearrange_words = " ".join(new_list)
    return rearrange_words


if __name__ == "__main__":
    input_words = sys.argv[1:]
    print(rearrange_words(input_words))
