from dictogram import Dictogram
from frequency import histogram_dictionary, open_file

def get_hisogram(): 
    path = '/Users/ysawiris/dev/CS-1.2-Intro-Data-Structures/tweet_generator/database/lyrcis.txt'
    text = open_file(path)
    histogram = histogram_dictionary(text)

    print(histogram)


if __name__ == "__main__":
    get_hisogram()