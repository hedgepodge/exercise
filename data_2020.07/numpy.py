import numpy as np

array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
print(array1)
array2 = array1[2:11:2]
print(array2)

array1 = np.full(6, 7)
print(array1)

array1 = np.full(6, 0)
array2 = np.zeros(6, dtype=int)
print(array1)
print(array2)

array1 = np.full(6, 1)
array2 = np.ones(6, dtype=int)

print(array1)
print(array2)

array1 = np.random.random(6)
array2 = np.random.random(6)

print(array1)
print(array2)

array1 = np.arange(6)
print(array1)

array1 = np.arange(2, 7)
print(array1)

array1 = np.arange(3, 17, 3)
print(array1)

# arithmetic operation
array1 = np.arange(10)
array2 = np.arange(10, 20)
print(array1 * 2)
print(array1 / 2)
print(array1 + 2)
print(array1 ** 2)
print(array1 + array2)
print(array1 * array2)
print(array1 / array2)

# Boolean
array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
print(array1 > 4)
print(array1 % 2 == 0)
booleans = np.array(True, True, False, True, True, False, True, True, True, False, True)
np.where(booleans)
filter = np.where(array1 > 4)
array1[filter]


# Target revenue
import numpy as np

revenue_in_yen = [
    300000, 340000, 320000, 360000,
    440000, 140000, 180000, 340000,
    330000, 290000, 280000, 380000,
    170000, 140000, 230000, 390000,
    400000, 350000, 380000, 150000,
    110000, 240000, 380000, 380000,
    340000, 420000, 150000, 130000,
    360000, 320000, 250000
]

yen_array = np.array(revenue_in_yen)

bad_days_revenue = yen_array[(np.where(yen_array <= 200000))]

# print answer
bad_days_revenue


array1 = np.array([14, 6, 13, 21, 23, 31, 9, 5])
print(array1.max())
print(array1.min())

array1 = np.array([14, 6, 13, 21, 23, 31, 9, 5])
print(array1.mean())

array1 = np.array([8, 12, 9, 15, 16])
array2 = np.array([14, 6, 13, 21, 23, 31, 9, 5])
print(np.median(array1))
print(np.median(array2))

array1 = np.array([14, 6, 13, 21, 23, 31, 9, 5])
print(array1.std())
print(array1.var())

