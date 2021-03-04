'''
implementation of how to use escape codes
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
test_phrase = 'This a string with some numbers 1233 and a symbol #hashtag'
test_patterns = [r'\d+',#sequence of digits
                 r'\D+',#sequence of non-digits
                 r'\s+',#sequence of whitespace
                 r'\S+',#sequence of non-whitespace
                 r'\w+',#sequence of alpha-numeric
                 r'\W+',#sequence of non-alphanumeric
] 
multi_re_find(test_patterns,test_phrase)