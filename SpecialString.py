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

