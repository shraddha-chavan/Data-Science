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


################################################################################
#2.^(caret)-matches start of string
print(re.findall(r"^Hello","Hello World\nHelllo Python"))
'''output:['Hello']

The regex pattern ^Hello is used to match the word 
"Hello" only if it appears at the very start of the string.
 In the expression re.findall(r"^Hello", "Hello World\nHelllo Python"),
 the caret ^ anchors the match to the beginning of the entire string,
 not after the newline \n, unless the re.MULTILINE flag is used
 (which it isn't here). So, even though the string has two lines, 
  only the first "Hello" at the beginning of the string is matched, 
  and the second one ("Helllo") is ignored because it doesn’t exactly
  match "Hello" and it's not at the start. Hence, the output is ['Hello'].

  '''
#####################################################################################

#3.$(dollar)-matches a=end of string
print(re.findall(r"Python$","Hello Python"))
'''output:['Python']

The regex pattern r"Python$" is used to check if 
the word "Python" appears at the end of a string,
 with the $ symbol representing the end of the string. 
 The function re.findall() searches for all 
 matches of this pattern in the provided string and 
 returns them as a list. For example, in the string 
 "Hello Python", the word "Python" is indeed at the end, 
 so the output is ['Python']. However, if the string was 
 "Hello Python is awesome", the output would be an empty 
 list ([]) because "Python" is not at the end. 
 This is how the pattern works simply and effectively!
'''
###########################################################################

#4.*(asterisk)-0 or more of the preceding character
print(re.findall(r"ab*c","ac abc abbc abbbc"))
'''output:['ac', 'abc', 'abbc', 'abbbc']'

Pattern: ab*c
(a → match the letter 'a'
b* → match zero or more 'b' letters (can be no 'b', or many)
c → match the letter 'c')

So, ab*c matches:
"ac"       (no b)
"abc"      (one b)
"abbc"     (two b's)
"abbbc"    (three b's)

  '''
###########################################################################

#5.+(plus)- 1 or more of the preceding character
print(re.findall(r"ab+c","ac abc abbc abbbc"))
'''output:['abc', 'abbc', 'abbbc']

Pattern: ab+c
(a → match the letter 'a'
b+ → match one or more 'b' (at least one 'b')
c → match the letter 'c')

It matches:
"abc" ✅ (1 b)
"abbc" ✅ (2 b’s)
"abbbc" ✅ (3 b’s)
"ac" ❌ (has no b, so doesn’t match)

'''
##########################################################################

#6.?(question)-0 or 1 preceding character
print(re.findall(r"ab?c","ac abc abbc abbbc"))
'''output:['ac', 'abc']


Pattern: ab?c
(a → match the letter 'a'
b? → match zero or one 'b' (can have no 'b' or just one)
c → match the letter 'c')

It matches:
"ac" ✅ (zero b)
"abc" ✅ (one b)
"abbc" ❌ (has two b's)
"abbbc" ❌ (has three b's)


'''

########################################################################










































































