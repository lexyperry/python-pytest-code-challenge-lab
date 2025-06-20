# lib/testing/test_palindrome.py

import pytest
from lib.palindrome import longest_palindromic_substring

# Basic Cases
def test_babad():
    assert longest_palindromic_substring("babad") in ["bab", "aba"]

def test_cbbd():
    assert longest_palindromic_substring("cbbd") == "bb"

# Edge Cases
def test_single_character():
    assert longest_palindromic_substring("a") == "a"

def test_two_unique_chars():
    assert longest_palindromic_substring("ac") in ["a", "c"]

def test_full_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"

def test_empty_string():
    assert longest_palindromic_substring("") == ""

def test_all_same_characters():
    assert longest_palindromic_substring("aaaa") == "aaaa"

def test_long_string_with_palindrome():
    long_input = "xyzracecarabc"
    assert longest_palindromic_substring(long_input) == "racecar"

# Numeric input
def test_numeric_input():
    assert longest_palindromic_substring("1234321") == "1234321"

# Mixed case sensitivity
def test_case_sensitivity():
    result = longest_palindromic_substring("Aa")
    assert result in ["A", "a"]

# No real palindrome longer than 1
def test_no_palindrome():
    input_str = "abcde"
    assert longest_palindromic_substring(input_str) in list(input_str)