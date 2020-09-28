"""Functions to manipulate strings."""


def greet_by_name(name):
    """Return a greeting to the given person."""
    if name:
        greeting = "Hello, " + name + "!"
    else:
        greeting = "Hello"
    return greeting


def reverse(string):
    """Reverses the characters in a string."""
    return string[::-1]


def reverse_words(string):
    """Reverses the letters in each word of a string."""
    if not string:
        return ""
    words = string.split()
    new_words = reverse(words[0])
    for word in words[1:]:
        new_words += " " + reverse(word)
    return new_words


def sarcastic(string):
    """ReTuRnS tHe SaRcAsTiC vErSiOn Of A sTrInG."""
    new_string = ""
    capitalize = True
    for letter in string:
        if letter.isalpha():
            new_string += letter.upper() if capitalize else letter.lower()
            capitalize = not capitalize
        else:
            new_string += letter
    return new_string


def find_longest_word(sentence):
    """Return the longest word in a sentence."""
    words_list = sentence.split()
    print(words_list)
    longest_word = ""
    for word in words_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
