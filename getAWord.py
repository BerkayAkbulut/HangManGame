import csv
import random


def get_a_word():
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    a_file = open(dir_path+"/"+"1-1000.txt", "r")

    list_of_lists = []
    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)

    chosenWord = random.choice(list_of_lists)
    return chosenWord