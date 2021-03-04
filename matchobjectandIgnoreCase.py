#re.search() returns a match object which also contains information about the start and the end of the match
#list of patterns to search for
import re 
pattern ="term1"
#text to parse
text = "This is a string with term1,but it doesnot  have the other term."
match  = re.search(pattern,text)
print(type(match))
print(match.start())
print(match.end())
text1 =  "This is a string with a Term1,but it doesnot  have the other term."
match1 = re.search(pattern,text,re.IGNORECASE)
print(match1.start())