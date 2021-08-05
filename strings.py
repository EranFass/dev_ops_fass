"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
### git comment    --> YG DONE ;-)
"""
import textwrap as tr

import pytest

# import re

def no_duplicates(a_string):
    ans = ''.join(sorted(set(a_string)))
    #print("Result sorted string with no duplicate characters: ", ans)
    return ans


def reversed_words(a_string):
    # YG solution 2:
    ## splitting the string on space
    words = a_string.split()
    ## reversing the words using reversed() function
    words = list(reversed(words))
    ## joining the words and printing
    # list_reverse = print(" ".join(words))
    return words
#YG solution 1: but BUG with test_reversed_words()...
    # # first split the string into words
    # words = a_string.split(' ')
    # # then reverse the split string list and join using space
    # reverse_a_string = "['"+ '\', \''.join(reversed(words)) + "']"
    # # finally return the joined string
    # return reverse_a_string


def four_char_strings(a_string):
    # list1 = re.findall('....', a_string)   # Good but 2 last caracteres missing...4,4,4,2...!
    lines = tr.wrap(a_string, width=4)
    return lines


def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', 'circ', 'us']

a_string = input("insert String:")
print("Result sorted string with no duplicate characters: ", no_duplicates(a_string))

print("Result that returns the words in reverse order: ", reversed_words(a_string))

print("Result that returns a list of 4 character strings: ", four_char_strings(a_string))

test_no_duplicates()
test_reversed_words()
test_four_char_strings()


"""
def main():
    return pytest.main(_file_)


if _name_ == '_main_':
    main()
"""