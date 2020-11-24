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