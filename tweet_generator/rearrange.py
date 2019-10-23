import random
import sys


def rearrange_words(input=sys.argv[1:]):
    input_list = list(range(len(input)))
    new_list = []

    while(len(input_list) != 0):
        random_list = random.randint(0, len(input_list) - 1)
        new_list.append(input[input_list[random_list]])
        input_list.pop(random_list)

    return new_list


if __name__ == "__main__":
    print(rearrange_words())
