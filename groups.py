#groups()
# we use groups(num) or groups() function of match object to get matched expression
import re
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)
if matchObj:
    print("matObj.group() :",matchObj.group())
    print("matObj.group() :",matchObj.group(1))
    print("matObj.group() :",matchObj.group(2))
else:
    print("No match !")