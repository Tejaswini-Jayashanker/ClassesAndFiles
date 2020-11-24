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