########## fibonacci sequence ##########
# return n-th fibonacci number
def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# test: print from fib(1) to fib(10)
for i in range(1, 11):
    print(fib(i))


########## fibonacci series ##########
# return the consecutive sum from 1 to n
def triangle_number(n):
    if n == 1:
        return n
    else:
        return triangle_number(n-1) + n

# test: print from triangle_number(1) to triangle_number(10)
for i in range(1, 11):
    print(triangle_number(i))


########## digits sum ##########
# return the sum of digits of n
def sum_digits(n):
    if n < 10:
        return n
    else:
        return n - n//10 * 10 + sum_digits(n // 10)

# test
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

#sample answer
def sum_digits(n):
    # base case
    if n < 10:
        return n

    # recursive case
    return n % 10 + sum_digits(n // 10)


########## flip list ##########
# flip some_list
def flip(some_list):
    a = []
    if len(some_list) < 2:
        return some_list
    else:
        return some_list[-1:] + flip(some_list[:-1])

# test
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)


########## binary search using recursive function ##########

def binary_search(element, some_list, start_index=0, end_index=None):
    if end_index == None:
        end_index = len(some_list) - 1
    if start_index > end_index:
        return None
    if element == some_list[(start_index + end_index) // 2]:
        return (start_index + end_index) // 2
    elif element > some_list[(start_index + end_index) // 2]:
        start_index = (start_index + end_index) // 2 + 1
        return binary_search(element, some_list, start_index, end_index)
    elif element < some_list[(start_index + end_index) // 2]:
        end_index = (start_index + end_index) // 2 - 1
        return binary_search(element, some_list, start_index, end_index)

# test
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

#sample answer
def binary_search(element, some_list, start_index=0, end_index=None):
    if end_index == None:
        end_index = len(some_list) - 1
    if start_index > end_index:
        return None
    mid = (start_index + end_index) // 2
    if some_list[mid] == element:
        return mid
    if element < some_list[mid]:
        return binary_search(element, some_list, start_index, mid - 1)
    else:
        return binary_search(element, some_list, mid + 1, end_index)


########## tower of hanoi ##########
def move_disk(disk_num, start_peg, end_peg):
    print("move %d th disk from %d th peg to %d th peg" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 0:
        return None
    else:
        hanoi(num_disks - 1, start_peg, 6 - start_peg - end_peg)
        move_disk(num_disks, start_peg, end_peg)
        hanoi(num_disks - 1, 6 - start_peg - end_peg, end_peg)

# test
hanoi(3, 1, 3)

#sample in wikipedia
def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, "->", to_pos)
        return
    hanoi(n - 1, from_pos, aux_pos, to_pos)
    print(from_pos, "->", to_pos)
    hanoi(n - 1, aux_pos, to_pos, from_pos)


