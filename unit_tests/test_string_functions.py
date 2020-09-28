"""Import pytest and functions to test."""
import pytest
from .string_functions import (
    greet_by_name,
    reverse,
    reverse_words,
    sarcastic,
    find_longest_word,
)


def test_greeting_jeremy():
    """Test for greet_by_name."""
    expected = "Hello, Jeremy!"
    actual = greet_by_name("Jeremy")
    assert actual == expected


def test_greeting_dani():
    """Test for greet_by_name."""
    expected = "Hello, Dani!"
    actual = greet_by_name("Dani")
    assert actual == expected


def test_greeting_edge_case():
    """Test for greet_by_name with an edge case."""
    expected = "Hello"
    actual = greet_by_name("")
    assert actual == expected


def test_reverse_long():
    """Test reversing a long string."""
    expected = "Tennessee"
    actual = reverse("eessenneT")
    assert actual == expected


def test_reverse_short():
    """Test reversing a short string."""
    expected = "oG"
    actual = reverse("Go")
    assert actual == expected


def test_reverse_edge_case():
    """Test reversing in an edge case."""
    expected = ""
    actual = reverse("")
    assert actual == expected


def test_reverse_words_long():
    """Test reversing words in a long string."""
    expected = "away. go to me told mother My"
    actual = reverse_words(".yawa og ot em dlot rehtom yM")
    assert actual == expected


def test_reverse_words_short():
    """Test reversing words in a short string."""
    expected = "Henry Prince"
    actual = reverse_words("yrneH ecnirP")
    assert actual == expected


def test_reverse_words_edge_case():
    """Test reversing words in an edge case."""
    expected = ""
    actual = reverse_words("")
    assert actual == expected


def test_sarcastic_long():
    """Test sarcastic-ifying a long string."""
    expected = "Is ThIs HeRe CoMpUtEr ThInG eVeN wOrKiNg?"
    actual = sarcastic("Is this here computer thing even working?")
    assert actual == expected


def test_sarcastic_short():
    """Test sarcastic-ifying a short string."""
    expected = "WhAt Is ThIs LaNgUaGe?"
    actual = sarcastic("What is this language?")
    assert actual == expected


def test_sarcastic_edge_case():
    """Test sarcastic-ifying an edge case."""
    expected = ""
    actual = sarcastic("")
    assert actual == expected


def test_find_longest_word_long():
    """Test find longest word with a long string."""
    expected = "sentence?"
    actual = find_longest_word("What is the longest word in this sentence?")
    assert actual == expected


def test_find_longest_word_short():
    """Test find longest word with a short string."""
    expected = "phrase"
    actual = find_longest_word("A short phrase to try.")
    assert actual == expected


def test_find_longest_word_edge_case():
    """Test find longest word with an edge case."""
    expected = ""
    actual = find_longest_word("")
    assert actual == expected


# run the tests
if __name__ == "__main__":
    unittest.main()
