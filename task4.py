def count_occurrences(input_string):
    char_count = {}

    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count

user_word = input("Pick a word \n")
user_word_char_count = count_occurrences(user_word)
print(user_word_char_count)