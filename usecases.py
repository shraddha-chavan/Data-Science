FindStringCode
Crazy Zak has designed the below steps which can be applied on any given string
(sentence), to produce a number.
Step1.In each word , find the Sum of the Difference between the first letter and the
last letter , second letter and the penultimate letter
STEP 2:Concatinate the sums of each word to form the result

for example: 
    If the given String is "WORLD WIDE WEB"
    
STEP 1:in each word , find the sum of the Difference between
the first letter and the last letter, second letter and the
 penultimate letter and so on till the center of the word 
 
 WORLD = [W-D]+[O-L]+[R] = [23-4]+[15-12]+[18]=[19]+[3]+[18]=[40]
 WIDE = [W-E]+[l-D]=[23-5]+[9-4]=[23]
 WEB = [W-B]+[E]=[23-2]+[5]=[26]

'''
sentence ='world wide web'
sentence = sentence.upper()
words = sentence.split()
words
#Convert each word into a list of characters
char_lists = [list(word) for word in words]
char_lists

#Extract first and last character from the list
first_char=char_lists[0][0]
last_char=char_lists[0][-1]

#Get ASCII values
ascii_first=ord(first_char)
ascii_last=ord(last_char)

print(f"First character : {first_char} ,ASCII:{ascii_first}")
print(f"Last character : {last_char} ,ASCII:{ascii_last}")

############################# 
sentence = 'world wide web'
sentence = sentence.upper()
words = sentence.split()
#Convert each word into a list of 
char_lists = [list(word) for word in words]
#Process each word and compute ASCII differences
ascii_differences = []

for word in char_lists:
    first_char = word[0]
    last_char = word[-1]
    ascii_first = ord(first_char)
    ascii_last = ord(last_char)
    
    difference = abs(ascii_first - ascii_last)
    ascii_differences.append(difference)

#Print results
for word,diff in zip(words,ascii_differences):
    print(f"Word:{word}, ASCII Difference:{diff}")
    
result = int("".join(map(str,ascii_differences)))
print(f"Final Output: {result}")    
###############################
sentence = 'world wide web'
sentence = sentence.upper()
words = sentence.split()

# Process each word
word_sum = [] #Store sum of ASCII differences for each word

for word in words:
    length = len(word)
    total = 0 # Sum of difference for this word
    
    for i in range((length+1)//2):
        first_char = word[i]
        last_char = word[length - 1 - i]
        total += abs(ord(first_char) - ord(last_char))
     
    word_sum.append(str(total)) # Store result as string 
    
#Concatenate the sums to form the final number
final_result = int("".join(word_sum))

#Print result
for word, word_sum in zip(words, word_sum):
    print(f"Word: {word}, Sum of Differences: {word_sum}")

print(f"Final Output: {final_result}")

#Convert letter to their mapped values (A=1, B=2,......., Z=26)
def get_mapped_value(letter):
    return ord(letter) - ord('A') + 1    

#Example 
letters = ['A', 'B', 'R', 'W', 'Z']
for letter in letters:
    print(f"Letter:{letter}, Mapped Value:{get_mapped_value(letter)}")
    
    
def findStringCode(sentence):
    sentence = sentence.upper()
    words = sentence.split()
    word_sum = [] #Store sum of ASCII differences for each word
    
    for word in words:
        length = len(word)
        total = 0 # Sum of ASCII difference for current word
        print(f"\nProcessing word: {word}")
        
        #Compute absolute difference using mapped values
        for i in range(length//2):
            first_char = word[i]
            last_char = word[length - 1 - i]
            '''
            Indexes: 0 1 2 3 4
                     W O R L D
            i   word[i]             word[length - 1 - i]
            0   'W'(Index 0)         'D' (Index 4)
            1   'O'(Index 1)         'L' (Index 3)
            2   'R'(Index 2)         'R' (Index 2)
            
            '''
        
            first_val = ord(first_char) - ord('A') + 1
            last_val = ord(last_char) - ord('A') + 1
        
            diff = abs(first_val - last_val)
            print(f"pair:({first_char}, {last_char}) -> ({first_val}-{last_val})={diff}")
            total += diff
            
        # If word length is odd, add the middle character value
        if length % 2 == 1:
            mid_char = word[length//2]
            mid_value = ord(mid_char) - ord('A') + 1 
            print(f"Middle Character: {mid_char}, Mapped Value:{mid_value}")
            total += mid_value
            
        print(f"Total for '{word}': {total}")
        word_sum.append(str(total))
        
    #Concatenate values to form the final result
    final_result = int("".join(word_sum))
    print(f"\nFinal Output: {final_result}") #Expected: 402326
    return final_result

#Example Usage
sentence = "WORLD WIDE WEB"
output = findStringCode(sentence)
###########################################################################
'''
Farah is one of the few associates in Global Safe
Lockers Corp Limited, who has access to the company's
exclusive locker that holds confidential information 
related to her division. The PIN to the locker gets
changed every two days. Farah receives the PIN in the
form of a string which she needs to decode to get the
single-digit numeric PIN.
The numeric PIN can be obtained by adding the lengths 
of each word of the string to get the total length,
and then continuously adding the digits of the total
length till we get a single digit.
For example, if the string is "Wipro Technologies", 
the numeric PIN will be 8.
Explanation:
Length of the word "Wipro" = 5
Length of the word "Technologies" = 12
Let us add all the lengths to get the Total Length = 5 + 12 = 17
The Total Length = 17, which is not a single-digit, so now let
us continuously add all digits till we get a single digit i.e. 1+ 7 = 8
Therefore, the single-digit numeric PIN = 8
Farah approaches you to write a program that would generate the
single-digit numeric PIN if the string is input into the program. Help Farah by writing the function (method) that takes as input a string input1 that represents the sentence, and returns the single-digit numeric PIN.
Assumptions: For this assignment, let us assume that the given string will always contain more than one word.
Let's see one more example-
If the given string is "The Good The Bad and The Ugly", the numeric PIN would be = 5
Explanation:
Let us add lengths of all words to get the Total Length = 3+4+3+3+3+3+4= 23 Total Length = 23, which is not yet a single digit, so let us continue adding all digits of the Total Length, ie. 2+3=5
Therefore, single-digit numeric PIN =5
If the given string is "The Good The Bad and The Ugly", the numeric PIN would be = 5
Explanation:
Let us add lengths of all words to get the Total Length = 3+4+3+3+3+3+4= 23 Total Length = 23, which is not yet a single digit, so let us continue adding all digits of the Total Length, ie. 2+3=5
Therefore, single-digit numeric PIN =5
'''
input1 = "Wipro Technologies"

# Step 1: Split into words
words = input1.split()

# Step 2: Convert words into lists of character
char_lists = [list(word) for word in words]
char_lists
# Step 3: Count letters in each list
letter_counts = [len(chars) for chars in char_lists]
letter_counts

print("Character Lists:",char_lists)
print("Letter Counts:",letter_counts)

def sum_digits(num):
    total = 0
    while num != 0:
        last_digit = num % 10
        total = total + last_digit # Set the last_digit
        num = num // 10 # Remove the last digit
    return total
    
print(sum_digits(456)) # Output: 15
total = [sum_digits(i) for i in letter_counts]
total
total_sum = 0
for i in total:
    total_sum = total_sum + i
total_sum   
########################
'''
For The Good the bad and the ugly output is wrong
''' 
input1 = "The Good the bad and the ugly"
words = input1.split()
char_list = [list(word) for word in words]
letter_count = [len(char) for char in char_list]
print(char_list)
print(letter_count)
def total_sum(num):
    total = 0
    while num != 0:
        last_digit = num % 10
        total = total + last_digit
        num = num // 10
    return total
total = [total_sum(num) for num in letter_count]
total
result = sum(total)
print("PIN:",result)    
#######################
'''Optimize Code'''
def get_pin(input1):
    words = input1.split()
    total_length = sum(len(word) for word in words)
    while total_length>=10:
        total_length=sum(int(digit) for digit in str(total_length))
    return total_length
get_pin('The Good the bad and the ugly')  
get_pin("Wipro Technologies")  
#####################################################################
#Part 1
'''
Encoding Three strings
Anand was assigned the task of comming up with
an encoding mechanism for any given three strings.
He has come up with the following plan.

Step1 :Spliting Each string into Three parts.
Given three input strings, break each string into three parts

Rules for Splitting:
If the string length is a multiple of 3,divide it into it into equal three parts
If the string length is not a multiple of 3:
If one extra character is present, assign it to middle part
If two extra characters are present, assign one extra character each to the front and end parts.
Example Splitting:
For input1 = 'John' (length = 4, i.e, 3+1)
For example - If the three strings are as below

Input1= "John"

Input2= "Johny

Input3= "Janardhan"

"John" should be split into "" "oh" "n" as the FRONT. MIDDLE and END parts respectively.

"Johny should be split into "lo" "h" "ny" as the FRONT, MIDDLE and END parts respectively.

"Janardhan" should be split into "Jan" "ard" "han" as the FRONT, MIDDLE and END parts respectively.

Le if the no of characters in the string are in multiples of 3, then each split-part will contain equal no of characters, as seen in the example of "Janardhan"

If the no of characters in the string are NOT in multiples of 3, and if there is one character more than multiple of 3. then the middle part will get the extra character, as seen in the example of "John"


'''
s1 = 'John'
s2 = 'Johny'
s3 = 'Janardhan'
lst = [s1, s2, s3]
char_list = [list(word) for word in lst]
for char in char_list:
    n=len(char)
    
    if n % 3 == 1: # 1 extra character goes to the middle
        first = char[:1]  
        middle = char[1:n-1] # Takes all except first
        end = char[n-1:] #Last character
        
    elif n % 3 == 2: # 1 extra charcater goes to first and end
        first = char[:2]
        middle = char[2:n-2] #Middle should take only one
        end = char[2:]
        
    else:# If n is exactly divisible by 3
        first = char[0:3]
        middle = char[3:6]
        end = char[6:9]
        
    print(f"First:{''.join(first)}, Middle:{''.join(middle)}, End:{''.join(end)}")    
#####################
#Part 2
'''

'''
s1 = 'John'
s2 = 'Jonhy'
s3 = 'Janardhan'
lst = [s1, s2, s3]

#To store the parts of each string
first_parts = []
middle_parts = []
end_parts = []

for word in lst:
    n=len(word)
    
    if n % 3 == 1:
        first = word[:1]
        middle = word[1:n-1]
        end = word[n-1:]
        
    elif n % 3 == 2:
        first = word[:2]
        middle = word[2:3]
        end = word[3:]
        
    else:
        first = word[:3]
        middle = word[3:6]
        end = word[6:]
        
    # Appeend to lists
    first_parts.append(first)
    middle_parts.append(middle)
    end_parts.append(end)

#Concatenating the extracted part
output1 = ''.join(first_parts)
output2 = ''.join(middle_parts)
output3 = ''.join(end_parts).swapcase() #Convert case

#Print Final outputs
print(output1) # Expected: "JJoJan"
print(output2) # Expected: "ohnard"
print(output3) # Expected: "NHYHAN"

################################################################
input1="The Good The Bad and The Ugly"
words=input1.split()
words
char_lists=[list(word)for word in words]
char_lists
letter_counts=[len(chars)for chars in char_lists]
letter_counts
def total_sum(num):
    total=0
    while (num!=0):
        last_digit=num%10
        total=total+last_digit
        num//=10
    return total
total=[total_sum(num)for num in letter_count]
total
result=sum(total)
print("PIN",result)

def get_pin(input1):
    word=input1.split()
    total_length=sum(len(word)for word in words)
    while total_length>=10:
        total_length=sum(int(digit)for digit in str(total_length))
    return total_length
get_pin("The Good The Bad and The Ugly")
get_pin("Wipro Technologies")
  
      
'''Adittion using strings :write a function that
takes two nus in string formate and forms a string containing
the sum of this two nos'''
def add_of_string(num1,num2):
    sum=str(int(num1)+int(num2))
    return sum
print(add_of_string(10,20))
    

'''Find the most frequently occuring digit in 
series '''
from collections import Counter
def most_frequent_digit(numbers):
    digit_count = Counter()
    for num in numbers:
        digit_count.update(str(num))
    max_frequency=max(digit_count.values())
    most_frequency=[int(digit) for digit,count in digit_count.items() if count==max_frequency]
    return most_frequency,max_frequency
numbers=[1234,1234,44678]
most_frequent,frequency=most_frequent_digit(numbers)
print(f'most frequent occuring digit:{most_frequent}')
      
  
'''To find palindrome if the digit  is not palindrom the remove 
then remove those digit print how many digits are removed '''
def find_digit_to_remove(input1):
    str_num=str(input1)
    #Check if n is already palindrom 
    if str_num == str_num[::-1]:
        return -1#no digit need to be removed
    #Try removing each digit one by one
    for i in range(len(str_num)):
        new_num = str_num[:i]+str_num[i+1:]
        #remove digit at index i
        if new_num == new_num[::-1]:
            return int(str_num[i])
    return -1 
print(find_digit_to_remove(12332))      
print(find_digit_to_remove(122332))      
print(find_digit_to_remove(133321))      
print(find_digit_to_remove(123))      


'''Array with n elements expcted to find
 sum of values that are present in non-prime
 indices of the array.
'''
def sum_non_prime(input1,input2):
    def is_prime(num):
        if num<2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
            return True
    total=0
    for i in range(input2):
            if not is_prime(i):
                total+=input1[i]
    return total
input1=[10,20,30,40,50,60,70,80,90,100]
input2=10
print(sum_non_prime(input1,input2))

''' '''
lst=[3,1,5,2,4,6,7,9,11,8,10,12,13,15,17,19]
lst=[1,3,5,7,11,13]#only odd nos
lst=[0,2,4,6,8,9]#only even nos
lst=[1,2,3,4,5,6,7,8,9]#odd and even alternate
lst=[2,4,5,6,8]#single odd
curr_len=0
curr_sum=0
max_len=0
longest_sums=0
for num in lst:
    if num%2!=0:
        curr_len+=1
        curr_sum+=num
    else:
        if curr_len >0:
            if curr_len>max_len:
                max_len=curr_len
                longest_sums=[curr_sum]
            elif curr_len==max_len:
                longest_sums.append(curr_sum)
            curr_len=0
            curr_sum=0
if curr_len>0:
    if curr_len>max_len:
        max_len=curr_len
        longest_sums=[curr_sum]
    elif curr_len==max_len:
        longest_sums.append(curr_sum)
print(sum(longest_sums)if longest_sums else -1)
       

    
lst=[3,-1,-2,5,-3,-4,-5,6,-7,-8,-9,-10,-11,-12]
curr_len=0
curr_sum=0
max_len=0
longest_sums=0
for num in lst:
    if num<0:
        curr_len+=1
        curr_sum+=num
    else:
        if curr_len >0:
            if curr_len>max_len:
                max_len=curr_len
                longest_sums=[curr_sum]
            elif curr_len==max_len:
                longest_sums.append(curr_sum)
            curr_len=0
            curr_sum=0
if curr_len>0:
    if curr_len>max_len:
        max_len=curr_len
        longest_sums=[curr_sum]
    elif curr_len==max_len:
        longest_sums.append(curr_sum)
print(sum(longest_sums)if longest_sums else -1)
       

def minminusproduct(input1,input2):
    min_num=min(input1)
    subtracted_array=[x-min_num for x in input1]
    result_array=[x*min_num for x in subtracted_array]
    return result_array
input1=[4,8,2,6]
input1=[4,4,4,4]
input1=[4,8,2,6]
input2=0
minminusproduct(input1,input2)
################################################################
lst = [3,1,5,2,4,6,7,9,11,8,10,12,13,15,17,19]
lst = [1,3,5,7,9,11]
lst = [2,4,6,8,10]
lst = [1,2,3,4,5,6,7]
lst = [1,3,5,7,2,4,6,8,9,11]
lst = [2,4,6,8,1,3,5,7,9]
lst = [1,3,5,2,7,9,11,2,13,15,17]
lst = [2,4,6,8,11,10,12]
lst = []
current_length = 0
current_sum = 0
max_length = 0
longest_sums = []

for num in lst:
    if num % 2 != 0: #Check if the number is odd
        current_length += 1 
        current_sum += num
        
    else:
        if current_length > 0:
            if current_length > max_length:
                max_length = current_length
                longest_sums = [current_sum] #Reset list with new longest sum
            elif current_length == max_length:
                longest_sums.append(current_sum) #Append if same
                
                
             #Reset for next sequence
            current_length = 0
            current_sum = 0
             
# Check the last sequence in case the list ends with odd numbers
if current_length > 0:
   if current_length > max_length:
       max_length = current_length
       longest_sums = [current_sum]
   elif current_length == max_length:
       longest_sums.append(current_sum)
       
# Print the result
print(sum(longest_sums) if longest_sums else -1)       
  
##OUTPUT##
'''
1.Basic:
lst = [3,1,5,2,4,6,7,9,11,8,10,12,13,15,17,19]
output:
lst = [1,3,5,7,9,11]
lst = [2,4,6,8,10]
lst = [1,2,3,4,5,6,7]
lst = [1,3,5,7,2,4,6,8,9,11]
lst = [2,4,6,8,1,3,5,7,9]
lst = [1,3,5,2,7,9,11,2,13,15,17]
lst = [2,4,6,8,11,10,12]
lst = []  
'''

