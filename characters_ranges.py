'''
implementation of how to use character sets
'''
import re
def multi_re_find(patterns,phrase):
    '''
    Takes a list of regex patterns
    prints a list of all matches
    Args:
        patterns(list<str>) -> list of patterns to be matched in the pattern
        phrase(str) -> string 
    Returns:
        print(list of all matches of pattern found in the string)
    '''
    for pattern in patterns:
        print("searching the phrase using the re check :%s"%pattern)
        print(re.findall(pattern,phrase))
        print('\n')
test_phrase = 'This is an example sentence .Lets see if we find some letters.'
test_patterns = ['[a-z]+',#sequences of lower case letters
                 '[A-Z]+',#sequences of upper case letters
                 '[a-zA-Z]+',#sequences of either upper or lower case letters
                 '[A-Z][a-z]+']# 1 uppercase letter followed by lower case letters 
multi_re_find(test_patterns,test_phrase)