########## max product from two card bundles ##########
def max_product(left_cards, right_cards):
    a = []
    for i in range(0, len(left_cards)):
        for j in range(0, len(right_cards)):
            a.append(left_cards[i] * right_cards[j])
    return max(a)


# test
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))

# !!!!!!!!!! sample answer !!!!!!!!!!
def max_product(left_cards, right_cards):
    max_product = -1

    for left in left_cards:
        for right in right_cards:
            max_product = max(max_product, left * right)

    return max_product


########## find the nearest path ##########
from math import sqrt

# function to measure the distance of two stores
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# function to find the nearest two stores
# def closest_pair(coordinates):
#     a = {}
#     for item in test_coordinates:
#         for jtem in test_coordinates:
#             if item == jtem:
#                 pass
#             else:
#                 a[item, jtem] = distance(item, jtem)
#     b = min(a)
#     c = [b[0],b[1]]
#     return c
def closest_pair(coordinates):
    pair = [coordinates[0], coordinates[1]]
    for i in range(len(coordinates)-1):
        for j in range(i+1, len(coordinates)):
            store1, store2 = coordinates[i], coordinates[j]
            if distance(store1, store2) < distance(pair[0], pair[1]):
                pair = [store1, store2]
    return pair

# test
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))


########## trapping rain ##########
def trapping_rain(buildings):
    c = 0
    for i in range(1, len(buildings)-1):
        a, b = 0, 0
        for j in range(i):
            a = max(a, buildings[j])
        for j in range(i+1, len(buildings)):
            b = max(b, buildings[j])
        d = min(a,b)
        c = c + max(0, d - buildings[i])
    return c

# test
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

# sample answer
def trapping_rain(buildings):
    total_height = 0

    for i in range(1, len(buildings) - 1):
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])

        upper_bound = min(max_left, max_right)

        total_height += max(0, upper_bound - buildings[i])

    return total_height

