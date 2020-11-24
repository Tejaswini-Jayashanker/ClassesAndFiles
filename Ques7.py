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

def random_permuted_list (list_size,low,high,num_permutations = 10):
    list1 = []
    for itr in range(list_size):
        list1.append(random.randint(low,high))
    return list1
     
print(random_permuted_list(10,0,100))
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