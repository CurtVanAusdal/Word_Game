
import argparse
from random import randint, shuffle
from collections import Counter
import random as rand

global correct_counter
correct_counter = 0



"""zip samplegamepley.txt and wordgame.py together
"""


def shuffle_word(word_length,file_in):
    '''takes in the length of word you want to shuffle, it returns it originally and shuffled'''
    # print(word_length, 'this is the word length trying to find')
    test_list = []
    liner = open(file_in,'r')
    lines = len(liner.readlines())
    # print(lines)
    liner.close()
    with open(file_in, 'r') as in_file:
        for index in range(lines):
            line = in_file.readline().strip()
            test_list.append(line)
    # print(test_list)
    correct_lenlist = []
    for word in test_list:
        if len(word) == word_length:
            correct_lenlist.append(word)

    if len(correct_lenlist) == 0:
        print('there is not word with this length in the file or test strip provided')
        return

    random_index = randint(0, len(correct_lenlist) - 1)

    guess_this_word = correct_lenlist[random_index]
    original_word = guess_this_word
    # print(original_word)

    guess_word_listed = list(guess_this_word)
    # print(guess_word_listed)

    shuffle(guess_word_listed)
    # print(guess_word_listed)

    shuffled_word = "".join(guess_word_listed)
    # print(shuffled_word)

    # print(len(shuffled_word))
    # print(len(original_word))

    return (original_word, shuffled_word)


def extract_digits(input_string):
    '''returns (shortest_word_length,longest_word,length)'''
    number2 = input_string.split(',')
    return_tup = int(number2[0]), int(number2[-1])
    # print(return_tup)
    return return_tup


def create_blanks(file_in,short_length,long_length,og_word):
    '''makes the grid of empty lists'''
    # print(short_length)
    # print(long_length)
    # print(og_word)
    # print(scrambled_word)

    global keys_exist
    count_og_word = Counter(og_word)
    # print(count_og_word)
    """word = 'burner'
    short_length = 3
    long_length = len(word)

    # Open the file and read lines into a list
    with open('words.txt', 'r') as file_in:
        line_list = [line.strip() for line in file_in]

    all_words_list = []

    # Iterate through the possible word lengths
    for count_up in range(short_length, long_length + 1):  # Adjust the range endpoint
        for line in line_list:
            if count_up == len(line) and Counter(line) <= Counter(word):
                all_words_list.append(line)"""

    liner = open('words.txt','r')
    lines = len(liner.readlines())
    # print(lines)
    liner.close()


    with open(file_in,'r') as file__in:
        line_list = [line.strip() for line in file__in]
    # print(line_list)
    all_words_list = []
    for count_up in range(short_length,long_length+1):
        for line in line_list:
            if count_up == len(line) and Counter(line) <= Counter(og_word):
                all_words_list.append(line)
    # print('all words',all_words_list)
    beg = "["
    end = "["
    quote = "'"
    dash = '-'
    emp = ''

    sorted_list = sorted(all_words_list, key = lambda x: len(x))
    # print(sorted_list,'full sorted list')
    biglist_display = []
    biglist_display_words = []
    for variable in range(short_length, long_length + 1):
        words_of_length_i = [dash * len(word) for word in all_words_list if len(word) == variable]
        words_correct_i = [word for word in all_words_list if len(word) == variable]
        # print(type(words_of_length_i))
        if words_of_length_i:
            cacheit = (" ".join(words_of_length_i))
            # print(words_of_length_i)
            biglist_display.append(words_of_length_i)
        if words_correct_i:
            biglist_display_words.append(words_correct_i)

    # for i in biglist_display_words:
    #
    #     print(i,'withwords')
    # for i in biglist_display:
    #     print(i)
    #     for j in i:
    #         print(j,len(j),'length')

    return(biglist_display,sorted_list,biglist_display_words) #biglist is a list you have to iterate through to rpint to the user the game. The other one is the actual list of words in the smae order


def guess_and_fill(listoflist_blanks,sorted_list,guess,scrambled_word,blanks_withwords):
    '''takes in the listof list created by blanks, also takes in a guess. if guess is right
    it fill sin the blanks in alphabetical order by size. If guess is wrong: Nothing happens exept is says sorry try again'''



    # print(sorted_list)
    if guess == 'q':

        print('Game Quit')
        print('Here were the all the correct words:')
        print(sorted_list)
        '''this is whe wy that the rubric and example says to print out after quitting so that's what I am doing, although I think
        it would be better if it printed it in the blanks'''


        exit()
    # print(blanks_withwords)
    # print(blanks_withwords[0][0])
    # print(guess)
    # print(sorted_list)
    # print(listoflist_blanks)


    if guess in sorted_list:
    #guess is correct




        global correct_counter

        correct_counter +=1
        # print(correct_counter,'counter')
        # print(len(sorted_list),'sorted list length')



    # if correct_counter == len(sorted_list):
    #     print(sorted_list)


        print('\n')
        print("Correct!")
        print('\n')
        print(scrambled_word)


        #rearrange the blanks to match
        # print(sorted_list)
        length_guess = len(guess)

        list2 = listoflist_blanks #blanks present
        list1 = blanks_withwords #words present

        # Element to copy (e.g., 'E')
        element_to_copy = guess

        # Iterate through list1 to find the element
        for row_idx, sublist in enumerate(list1):
            for col_idx, element in enumerate(sublist):
                if element == element_to_copy:
                    # Copy the element to the same position in list2
                    list2[row_idx][col_idx] = element_to_copy

        # Print the updated list2

        for row in list2:
            print(row)



        new_blanks = listoflist_blanks



        # if correct_counter == len(sorted_list):
        #     print("Congraulations, you won the game!")
        #     return (guess_and_fill(listoflist_blanks, sorted_list, 'q', scrambled_word, blanks_withwords))

        return(guess_and_fill(new_blanks,sorted_list,input('Enter a guess: '),scrambled_word,blanks_withwords))
    else:
        print('\n')
        print("Sorry, try again!")
        print('\n')
        print(scrambled_word)
        [print(i) for i in listoflist_blanks]
        new_blanks = listoflist_blanks
        return(guess_and_fill(new_blanks,sorted_list,input('Enter a guess: '),scrambled_word,blanks_withwords))

def shuffle_one_word(word):
    '''Shuffles a single word returns the shuffled word whether or not it exists in the file words.txt'''

    list_it = list(word)
    # print(list_it)
    rand.shuffle(list_it)
    # print(list_it)

    shuffle_complete_word = ''
    for index in list_it:
        shuffle_complete_word += index

    # print(shuffle_complete_word)
    return shuffle_complete_word




def main():
    parser = argparse.ArgumentParser(description='Greet the user')
    parser.add_argument('word', type=str, nargs='?', help='Word given as an argument')
    args = parser.parse_args()

    if args.word:
        word_in = args.word

        shuffle_single_word = shuffle_one_word(word_in)
        blanky = create_blanks('words.txt',1,len(word_in),shuffle_single_word) #return (biglist_display,sorted_list,biglist_display_words)
        print(shuffle_single_word)
        print('\n')
        for index in blanky[0]:
            print(index)
        print('\n')
        game = guess_and_fill(blanky[0],blanky[1],input('Enter a guess: '),shuffle_single_word,blanky[2])

    else:
        # print("Hello, world!")
        ask_length = input('Enter the range of word lengths (low,high):')  # asks the user for a shortest and longest word length
        short_long = extract_digits(ask_length)  # uses extract digits to interpret input as integers, returns both shortest and longet length
        shuffle_it = shuffle_word(short_long[-1],'words.txt') #finds a word with len = longest possible length. Returns original word it found and that word in scrambled form
        print(f'{shuffle_it[1]}:') #presents the user with the word to unshuffle
        print('\n')
        blanks = create_blanks('words.txt',short_long[0],short_long[1],shuffle_it[0])
        for i in blanks[0]:
            print(i)
        print('\n')
        guess_and_fill(blanks[0],blanks[1],input('Enter a guess: '),shuffle_it[1],blanks[2])

if __name__ == "__main__":
    main()