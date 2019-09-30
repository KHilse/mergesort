import random

def merge(ls1, ls2):
    '''Helper function for MergeSort
    This function assumes both source arrays are sorted,
    then builds a result array by comparing the first
    elements from each and storing the lower one'''
    result = []
    while ls1 and ls2:
        if ls1[0] < ls2[0]:
            result.append(ls1.pop(0))
        else:
            result.append(ls2.pop(0))
    return result + ls1 + ls2

def MergeSort(ls):
    '''Sorts the input list using a recursiv
    mergesort algorithm'''
    if len(ls) > 1:
        mid = len(ls) // 2
        return merge(MergeSort(ls[:mid]),MergeSort(ls[mid:]))
    else:
        return ls



#print(merge([3,5,7,9],[2,4,6,8,10,12]))    
print(MergeSort([7,13,2,9,17,4,6,1]))
print(MergeSort([]))

random_list = []
for _ in range(1000):
    random_list.append(int(random.random()*1000))

print(MergeSort(random_list))