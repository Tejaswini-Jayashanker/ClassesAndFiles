#Assignment-4
''' This is a Solution to the given Problem Statement.
Define a class SpecialString that takes the parameter string for its constructor. Define a method
print_string for SpecialString that prints the string in a boundary like this
***************************
* Hello this is my string *
***************************
'''

class SpecialString:
    def __init__(self, string):
        self.string = string
        self.string_len = len(string)
    def print_string(self):
        for i in range(0,self.string_len + 4):
            print("*",end="")

        print("\n* " + self.string + " *")

        for i in range(0,self.string_len + 4):
            print("*",end="")
        return

str_in = input("Enter a String: ")
strobj = SpecialString(str_in)
strobj.print_string()

''' This is a solution to the given Problem Statement:
Write a function class_practice(value1,value2) that instantiates an object of SpecialString
with value1 , then calls print_string . Thereafter change the value inside the same object with
value2 and call `print_string`` again.
'''
class SpecialString:
    def __init__(self, string):
        self.string = string
        self.string_len = len(self.string)
    def print_string(self):
        for i in range(0,self.string_len + 4):
            print("*",end="")

        print("\n* " + self.string + " *")

        for i in range(0,self.string_len + 4):
            print("*",end="")
        print()
        return
    def class_practice(self, value1, value2):
        self.string = value1
        self.string_len = len(self.string)

        self.print_string()
        
        self.string = value2
        self.string_len = len(self.string)
 
        self.print_string()
        return

str_in = input("Enter a String: ")
strobj = SpecialString(str_in)
strobj.print_string()

val1 = input("Enter Value 1: ")
val2 = input("Enter Value 2: ")

strobj.class_practice(val1, val2)

###################################################### The below method was discussed in yesterday's class, with correct implementation.
'''
from SpecialStringfile import SpecialString as S

def class_practice(self, value1, value2):
    ss_obj  = S(value1)
    ss_obj.print_string()
    ss_obj.string = value2
    ss_obj.print_string()
'''


'''This is a solution to a given Problem statement:
Write a function record_notes() that does the following
A. First asks the user's name.
B. Asks the user to enter a single-line note. After the user enters the note, it is stored in
USERNAME_notes.txt on a newline.
C. Keeps asking the user to enter a note in a loop, or to type "exit" to exit the program.
D. Make sure that killing the program suddenly doesn't result in losing all the notes entered till that point.
E. You should be able to call record_notes() multiple times without deleting previous notes.
'''
import os

def record_notes():
    user_name = input("Enter your name: ")
    user_name = user_name + ".txt"
    os.path.isfile('./user_name')
    with open ( user_name, 'a+') as filePointer:
        while( True):
            text_input = input("Enter a Single Line Note: ")
            if( text_input == "exit"):
                print("Exiting")
                break;
            else:
                filePointer.write(text_input)
                filePointer.write("\n")

record_notes()  


'''This is one approach to the given Problem Statement:
Write a function read_notes() that does the following
A. First asks the user's name.
B. Asks the user to enter a word.
C. Print all the notes with that word in the user's notes, as created using record_notes() .

record_notes :
Write a function record_notes() that does the following
A. First asks the user's name.
B. Asks the user to enter a single-line note. After the user enters the note, it is stored in
USERNAME_notes.txt on a newline.
C. Keeps asking the user to enter a note in a loop, or to type "exit" to exit the program.
D. Make sure that killing the program suddenly doesn't result in losing all the notes entered till that point.
E. You should be able to call record_notes() multiple times without deleting previous notes.
'''
import os.path
from os import path

def read_notes():
    user_name = input("Enter your name: ")
    user_name += ".txt"
    if( path.exists(user_name) ):
        with open(user_name, 'r') as ReadfilePointer:
            search_word = input("Enter a Word to search: ")
            for line_string in ReadfilePointer:
                if( search_word in line_string):
                    print(line_string)
    else:
        print("No Such File or Directory to read.")

read_notes()

'''This is one solution to the given Problem Statement:
Read the file passage.txt and perform the following operations in a function called
process_passage()
A. Print the number of characters in the whole file.
B. Find all the unique words in the file. Remember words may be divided by spaces or punctuation.
C. Find the list of (start,end) positions of each unique word in terms of characters from the beginning of
the file. (Hint: You can find all occurrences of a substring in a string by repeated calls to the find
method, increasing the beg parameter after each call.)
D. Write the information regarding unique word vs (start,end) positions as a JSON file
passage_info.json .
'''

import json

def process_passage():
    number_words = 0
    with open("passage.txt", 'r') as ReadFilePointer:
        for read_line in ReadFilePointer:
            list_words = read_line.split()
            number_words += len(list_words)
        ReadFilePointer.seek(0)
        text_str = ReadFilePointer.read()

    text_str = text_str.lower()
    words = text_str.split()
    words = [word.strip('.,!;()[]\\\'\"|') for word in words]

    unique_words_list = []
    for word in words:
        if word not in unique_words_list:
            unique_words_list.append(word)

    result_list = []
    res_dict = {}
    fin_dict = {}
    cnt = 0
    with open("passage_info.json", 'w+') as WriteFilePointer:
        for itr_word in unique_words_list:
            for i in range( len(text_str) ):
                if text_str.startswith(itr_word, i):
                    result_list.append( [ i, i + len( itr_word ) ] )
            if res_dict.get(itr_word) is None:    
                res_dict[itr_word] = []
                res_dict[itr_word].append( result_list )
            fin_dict.update(res_dict)
            res_dict = { }
            result_list = [ ]  
        json.dump(fin_dict,WriteFilePointer)
        
    return number_words, unique_words_list

if __name__ == '__main__':
    no_words, list_words = process_passage()
    print("No of Words in the File: ",no_words)
    print("Unique Word List :",list_words)


'''This is one solution to the given Problem Statement:
-------------------------------------------------------------------------------------------------------------
5. Read the file passage.txt and perform the following operations in a function called
process_passage()
A. Print the number of characters in the whole file.
B. Find all the unique words in the file. Remember words may be divided by spaces or punctuation.
C. Find the list of (start,end) positions of each unique word in terms of characters from the beginning of
the file. (Hint: You can find all occurrences of a substring in a string by repeated calls to the find
method, increasing the beg parameter after each call.)
D. Write the information regarding unique word vs (start,end) positions as a JSON file
passage_info.json .
---------------------------------------------------------------------------------------------------------------
6. Write a function view_word_examples(word,surrounding_chars,max_examples) that does the
following
A. Read the information from passage_info.json .
B. Given the word, check if it is one of the unique words, if not print "No examples found".
C. If yes, print an example of the word from passage.txt with surrounding_chars number of
characters of the surrounding text on both sides.
For example, if word is "geological" and surrounding_chars=10, then the first example
should be "terval of geological time from" (10 bytes extra on both sides)
D. Print at most max_examples number of examples.

Do not reiterate over the file passage.txt looking for the words in this question, reuse the
preprocessing from the previous step. In real life as well, many times you will want to do this
kind of preprocessing so that you can save the time of the user. Do not use seek() method, as
len(fi.read(num_bytes))!=num_bytes always (as some characters take multiple bytes to encode)
'''
import Passage_Processing as PP
import json

def view_word_examples(word,surrounding_chars,max_examples):
    i = 0
    j = 0
    with open("passage_info.json",'r') as readFilePointer:
        file_read_dict = json.load(readFilePointer)
        word = word.lower() #previously converted to lower case before storing the key to dictionary

        if word in file_read_dict.keys():
            with open("passage.txt", 'r') as pasReadPointer:
                file_text = pasReadPointer.read()
            value = []
            print("Key Exists")
            value = file_read_dict.get(word)
            while( i < max_examples):
                start_index = (value[0][i][j] - surrounding_chars -  len(word) )
                end_index = ( value[0][i][j] + surrounding_chars + len(word ) )
                print( file_text[start_index : end_index + 1 ] )
                i += 1
                j = 0
        else:
            print("This Key Does not exist!")

view_word_examples("first",5,2)


''' This is a solution to given problem statement
Write a function random_permuted_list(list_size,low,high,num_permutations) that
A. firstly generates a list of list_size random integers between low and high .
(hint: random.randint )
B. permute/shuffle the list num_permutations times and print each permutation out (hint:
random.shuffle )
'''
import random
'''
PART - 1
'''
def random_permuted_list (list_size,low,high,num_permutations = 10):
    list1 = []
    for itr in range(list_size):
        list1.append(random.randint(low,high))
    return list1
     
print(random_permuted_list(10,0,100))

'''
PART - 2
'''
def random_permuted_list (list_size,low,high,num_permutations = 10):
    list1 = []
    for itr in range(list_size):
        list1.append(random.randint(low,high))
    print("Initial List: ",list1)
    
    for itr_1 in range (num_permutations):
        random.shuffle(list1)
        print(itr_1,":", list1)
        
    return list1

print("Random Permuted Lists are :",random_permuted_list(10,0,100))


''' This is a solution to Ques 8.
Write a function generate_unique_numbers(num_unique,low,high) which uses the
random.randint function to generate random integers between low and high (both included).
Keep calling random.randint until num_unique unique numbers are generated. Use a list and
the membership operator for this step.
generate_unique_numbers should return a) the list of unique numbers b) the time taken to
generate the list (hint : time.time())
Add a boolean parameter use_set that specifies whether to use a set or a list to keep track of the
unique numbers generated so far.
Write in the comments which is faster : set or list? Why?
'''
import random
import time
'''
PART  - 1 
'''
def generate_unique_numbers(num_unique,low,high):
    if high - low < num_unique:
        return "Incorrect Input"
    else:
        list1 = []
        while len(list1) <= num_unique:
            var_check = random.randint(low, high)
            if var_check not in list1:
                list1.append( var_check )
        print("List is: ",list1)
        
'''
PART - 2 
'''    

def generate_unique_numbers(num_unique,low,high):
    if high - low < num_unique:
        return "Incorrect Input"
    else:
        list1 = []
        start = time.time()
        while len(list1) <= num_unique:
            var_check = random.randint(low, high)
            if var_check not in list1:
                list1.append( var_check )
        end = time.time() - start
    return end, list
        print("List is: ", list1)
'''  
PART - 3:
'''
def generate_unique_numbers(num_unique,low,high,flag_set):
    if high - low < num_unique:
        return "Incorrect Input"
    if not flag_set:
        list1 = []
        start = time.time()
        while len(list1) <= num_unique:
            var_check = random.randint(low, high)
            if var_check not in list1:
                list1.append( var_check )
        end = time.time() - start
        print(this list1)
    else:
        set_1 = set()
        start = time.time()
        while len(set_1) <= num_unique:
            set_1.add(random.randint(low,high))
            
 
print(generate_unique_numbers(45,10,15))
#Set is faster as set does not allow duplication.

