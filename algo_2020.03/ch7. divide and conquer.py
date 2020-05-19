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
