#Regular expressions supports a huge variety of patterns to find where a single string occured.
#Since we will be testing multiple re syntax forms, let's create a function that will print out results given a list of various regular expressions and a phrase to parse.
import re
def multi_re_find(patterns,phrase):
    '''
    Takes a list of regex patterns
    prints a list of all matches
    '''
    for pattern in patterns:
        print("searching the phrase using the re check : %s"%pattern) 
        print(re.findall(pattern,phrase))
        print('\n')