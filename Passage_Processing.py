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