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