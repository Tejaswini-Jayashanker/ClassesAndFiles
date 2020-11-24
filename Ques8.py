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