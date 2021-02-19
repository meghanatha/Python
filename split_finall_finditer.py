# re.split() -> returns a list with the term to split on removed and the terms in the list are a split up version of the string.
#Term to split on
import re
split_term = '@'
phrase = 'what is the domain of source with the email:hello@gmail.com'
#split on phrase
print(re.split(split_term,phrase))
# you can use re.findall() to find all the instances of a pattern in a string and returns the list
print(re.findall('match','test phrases match is in match middle'))
print(re.finditer('match','test phrases match is in match middle'))# finditer returns an iterator over all matches of the pattern in the string.
print(list(re.finditer('match','test phrases match is in match middle')))