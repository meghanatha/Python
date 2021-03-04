#escapes are indicated by prefixing the character with a blackslash (\)
#Unfortunable,a blackslash must itself be escaped in normal python strings,and that results in expressions that are diffcult to read
#Using raw strings,created by prefixing the literal value with r, for creating regular expressions eliminate this problem and maintains readability
'''
code            Meaning
\d              a digit
\D              a non-digit
\s              whitespace(tab,space,newline etc..,)
\S              non-whitespace
\w              alphanumeric
\W              non-alphanumeric
''' 