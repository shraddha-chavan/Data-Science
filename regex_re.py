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

#7.{}(curly braces)-exact or range og repetitions
print(re.findall(r"ab{2}c","ac abc abbc abbbc"))
'''output:['abbc']

Pattern: ab{2}c
(a → match the letter 'a'
b{2} → match exactly two bs (no more, no less)
c → match the letter 'c')

It matches:
"ac" ❌ (no b's)
"abc" ❌ (only one b)
"abbc" ✅ (exactly two b's)
"abbbc" ❌ (three b's)

'''
########################################################################
#8.[](square brackets)-either b or c character set
print(re.findall(r"a[bc]d","abd acd aad aed"))
'''output:['abd', 'acd']

Pattern: a[bc]d
(a → match the letter 'a'
[bc] → match either 'b' or 'c' (this is a character set, so either one will work)
d → match the letter 'd')

It matches:
"abd" ✅ (matches 'b' from the set [bc])
"acd" ✅ (matches 'c' from the set [bc])
"aad" ❌ (doesn’t match 'b' or 'c' in the middle)
"aed" ❌ (doesn’t match 'b' or 'c' in the middle)
'''
#######################################################################################


#9.[^](negated set)-not in the set
print(re.findall(r"a[^bc]d","aad aed acd abd"))
'''output:['aad', 'aed']
Pattern: a[^bc]d
(a – the word must start with a
[^bc] – the middle letter cannot be b or c
d – the word must end with d)

Text: "aad aed acd abd"
aad – middle is a (not b or c) → ✅ match
aed – middle is e (not b or c) → ✅ match
acd – middle is c → ❌ no match
abd – middle is b → ❌ no match

'''

####################################################################################

#10.|(pipe)-logical OR
print(re.findall(r"cat|dog","I have a cat and a dog"))
''' output:['cat', 'dog']

🔹 What it does:
cat|dog means: find "cat" or "dog"

The sentence is: "I have a cat and a dog"

It finds:
cat ✅
dog ✅


'''

###################################################################################

#11.()(parentheses)-grouping
print(re.findall(r"(ab)+","abab ab ababab"))
'''output:['ab', 'ab', 'ab']

Pattern: (ab)+
() → groups ab
+ → match one or more times

Text: "abab ab ababab"
'abab' → has 'ab' twice → ✅ group is 'ab'
'ab' → one 'ab' → ✅ group is 'ab'
'ababab' → three 'ab' → ✅ group is 'ab'


'''
##############################################################################
#12.\d-digit
print(re.findall(r"\d+","123 abc 234"))
'''output:['123', '234']
these pattern gives alll the digits present in the pattern


Regex: \d+
\d – matches any digit (0-9)
+ – means one or more digits

So, \d+ matches all sequences of digits in the text.

Text: "123 abc 234"

"123" → has digits 123 → ✅ Match
"abc" → no digits → ❌ No match
"234" → has digits 234 → ✅ Match

'''

###############################################################################


#13.\D-non-digit
print(re.findall(r"\D+","123 abc 234"))
'''output:[' abc ']

Regex: \D+
\D – matches any non-digit (anything that is not 0-9)
+ – means one or more non-digit characters

So, \D+ matches sequences of non-digit characters.

Text: "123 abc 234"

"123" → all digits → ❌ No match
" abc " → has spaces and letters → ✅ Match
"234" → all digits → ❌ No match




'''
##################################################################################


#14.\w-word character(alphanumeric + _)
print(re.findall(r"\w+","a_b 123 @!"))
'''output:['a_b', '123']

Regex: \w+
\w – matches word characters, which include:
Alphanumeric characters (letters and numbers)
Underscore (_)
+ – means one or more of the above characters

So, \w+ matches sequences of alphanumeric characters or underscores.

Text: "a_b 123 @!"

"a_b" → has letters and an underscore → ✅ Match
"123" → has digits → ✅ Match
"@!" → special characters, not alphanumeric or underscore → ❌ No match
'''
######################################################################
#15.\W-non-word character
print(re.findall(r"\W+","a_b 123 @!"))
'''OUTPUT:[' ', ' @!']

Regex: \W+
\W – matches non-word characters, which include:
Anything that is not alphanumeric (letters, digits) or an underscore (_)
+ – means one or more of the non-word characters

So, \W+ matches sequences of non-word characters.

Text: "a_b 123 @!"

"a_b" → is a word (alphanumeric + underscore) → ❌ No match
"123" → digits (word characters) → ❌ No match
" @!" → contains a space and special characters (@!) → ✅ Match


'''

########################################################################################

#16.\s-whitespace
print(re.findall(r"\s+","a b\tc\nd"))
'''output:[' ', '\t', '\n']

Regex: \s+
\s – matches whitespace characters, which include:
Space (' ')
Tab ('\t')
Newline ('\n')
Other whitespace characters like carriage return ('\r'), etc.
+ – means one or more whitespace characters

So, \s+ matches sequences of whitespace characters.

Text: "a b\tc\nd"
"a" → no whitespace → ❌ No match
" " (space) → whitespace → ✅ Match
"\t" (tab) → whitespace → ✅ Match
"\n" (newline) → whitespace → ✅ Match
"d" → no whitespace → ❌ No match



'''
################################################################################

#17.\S - non-whitespace
print(re.findall(r"\S+","a b\tc\nd"))
'''output:['a', 'b', 'c', 'd']

Regex: \S+
\S – matches non-whitespace characters, which include:
Letters, digits, and special characters (anything except spaces, tabs, and newlines)
+ – means one or more of these non-whitespace characters
So, \S+ matches sequences of non-whitespace characters.

Text: "a b\tc\nd"

"a" → non-whitespace → ✅ Match
"b" → non-whitespace → ✅ Match
"\t" (tab) → whitespace → ❌ No match
"c" → non-whitespace → ✅ Match
"\n" (newline) → whitespace → ❌ No match
"d" → non-whitespace → ✅ Match

'''
###############################################################################################

#18.re.sub()-substitude using regex
text="My number is 123-456-7890"
print(re.sub(r"\d{3}-\d{3}-\d{4}","***-***-****",text))
'''output:My number is ***-***-****

re.sub():
Function: re.sub(pattern, replacement, string)
It replaces occurrences of the pattern in the string with the specified replacement.

Regex: \d{3}-\d{3}-\d{4}
\d{3} – matches exactly three digits

- – matches the hyphen -

\d{4} – matches exactly four digits

So, \d{3}-\d{3}-\d{4} matches a phone number in the format: xxx-xxx-xxxx.

Text: "My number is 123-456-7890"

Find the phone number 123-456-7890
Replace it with ***-***-****


'''
##############################################################################################
#example
text="Call me att 987-654-3210 or at the office 123-456-7890"
re.sub(r"\d{3}-\d{3}-\d{4}","***-***-****",text)
'''ouput:'Call me att ***-***-**** or at the office ***-***-****'
'''
#################################################################################################

#19.re.split()-split by pattern
print(re.split(r"[,;]","apple,banana;grape,orange"))
'''output:['apple', 'banana', 'grape', 'orange']


re.split():
Function: re.split(pattern, string)
It splits the string wherever the pattern matches and returns a list of substrings.

Regex: [,;]
[,] – matches a comma ,
[;] – matches a semicolon ;

So, [,;] matches either a comma or a semicolon.

Text: "apple,banana;grape,orange"
The function will split the string wherever it finds a comma or semicolon.

It splits the string into the following parts:
"apple", "banana", "grape", "orange"


'''
#########################################################################################################

#20.\b matches:
#before the first letter/no. of a word
text="Hello world! Welcome to regex."
matches=re.findall(r"\b\w+\b",text)
print(matches)    
'''output:['Hello', 'world', 'Welcome', 'to', 'regex']

Regex: \b\w+\b
\b – word boundary. It matches the position before the first letter or number of a word.
\w+ – matches one or more word characters (letters, digits, or underscore).
The second \b – matches the position after the last letter or number of a word.

So, this pattern matches whole words in the text.

Text: "Hello world! Welcome to regex."

"Hello" → ✅ Match
"world" → ✅ Match
"Welcome" → ✅ Match
"to" → ✅ Match
"regex" → ✅ Match

'''
#####################################################################
#example:
text="Hello world Welcome to regex."
matches=re.findall(r"\bworld\b",text)
print(matches)    
    
'''output:['world']'''

######################################################################





















































































































































































