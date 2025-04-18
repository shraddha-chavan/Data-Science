#pip install regex
import re
#1..(dot)-matches any character except newline
print(re.findall(r"a.c","abc aac acc adc a-c"))
'''output:['abc', 'aac', 'acc', 'adc', 'a-c']'

1. re.findall(pattern, string)
Finds all non-overlapping matches of the pattern in the string.

Returns a list of matching substrings.

2. r"a.c" – The regex pattern:
r"" is a raw string literal, used so that backslashes in the regex don't need to be escaped.

"a.c" means:

a → Match literal 'a'

. → Match any single character (except newline \n)

c → Match literal 'c'

So a.c matches any three-character string that:

Starts with 'a'

Ends with 'c'

Has any one character in between.

'''
