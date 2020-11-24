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