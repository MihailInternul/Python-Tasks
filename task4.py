# Given an input string, count occurrences of all characters within a string (e.g. pythonnohtyppy -> p:3, y:3, t:2, h:2, o:2, n:2).

def count_occurrences(input_string):
    char_count = {}

    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count

user_word = input("Pick a word \n")
user_word_char_count = count_occurrences(user_word)
print(user_word_char_count)
