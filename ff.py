import itertools
lis_op = ['+', '-', '/', '*']

def separate_list(original_list):
    even_index_elements = original_list[::2]
    odd_index_elements = original_list[1::2]
    return even_index_elements, odd_index_elements

def interleave_lists(list1, list2):
    result = [item for pair in  itertools.zip_longest(list1, list2) for item in pair]
    return result

def bubblesort(alist):
    y = 0
    for x in range(len(alist)-1,0,-1):
        for i in range(x):
#            if y == 5:
#                exit()
#            if alist[i+1]  in lis_op:
#                y = y + 1
#                temp = alist[i+1]
#                alist[i+1] = alist[i]
#                alist[i] = temp

#                print(alist)

            if alist[i]  in lis_op:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp

                print(alist)
list = input()
alist  = list.split()

original_list = alist
even_list, odd_list = separate_list(original_list)
print("Lista original: ", original_list)
print("Elementos de índice par: ", even_list)
print("Elementos de índice ímpar: ", odd_list)
odd_list.reverse()

interleaved_list = interleave_lists(even_list, odd_list)
interleaved_list.remove(None)
print("Lista intercalada: ", interleaved_list)

bubblesort(interleaved_list)

