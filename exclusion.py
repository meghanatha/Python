# we can use ^ to exclude terms by incoroporating it into the brackets syntax notation.
#Use [^!.? ] to check for matches that are not a !,.? or space . Add + to check that the match appears at-least once,this basically translates to finding the words.
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
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print(re.findall('[^!.? ]+',test_phrase),end = " ")