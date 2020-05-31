########## consecutive sum using divide and conquer ##########
def consecutive_sum(start, end):
    mid = (start + end) // 2
    if start == end:
        return start
    else:
        return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)

# test
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))


########## merge two lists ##########
def merge(list1, list2):
    merged_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1
    merged_list += list2[j:] + list1[i:]
    return merged_list

# test
print(merge([1], []))
print(merge([], [1]))
print(merge([2], [1]))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
print(merge([4, 7, 8, 9], [1, 3, 6, 10]))


########## merge and sort two lists ##########
# merge sort
def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list
    else:
        left_half = my_list[:len(my_list) // 2]
        right_half = my_list[len(my_list) // 2:]
        my_list = merge(merge_sort(left_half), merge_sort(right_half))
        return my_list

# test
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))


########## partition function ##########
# helper function to swap two elements
def swap_elements(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

# partition function used in quicksort
def partition(my_list, start, end):
    i, b = start, start
    p = end
    while i < p:
        if my_list[i] < my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
            i += 1
        else:
            i += 1
    swap_elements(my_list, b, p)
    return b
        
# sample answer
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def partition(my_list, start, end):
    i = start
    b = start
    p = end

    while i < p:
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1

    swap_elements(my_list, b, p)
    p = b

    return p

# test 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# test 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)


########## quicksort ##########
# quicksort function
def quicksort(my_list, start, end):
    # base case
    if end - start < 1:
        return
    else:
        pivot = partition(my_list, start, end)
        quicksort(my_list, start, pivot-1)
        quicksort(my_list, pivot+1, end)


# test 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# test 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# test 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)


########## simpler quicksort ##########
# quicksort (without calling start, end parameters)
def quicksort(my_list, start=0, end = None):
    # base case
    if end == None:
        end = len(my_list) - 1
    if end - start < 1:
        return
    pivot = partition(my_list, start, end)
    quicksort(my_list, start, pivot-1)
    quicksort(my_list, pivot+1, end)

# test 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1)
print(list1)

# test 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2)
print(list2)

# test 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3)
print(list3)
