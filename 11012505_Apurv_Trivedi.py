import numpy as np

#1

arr1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
result = np.where(arr1 % 2 == 0,arr1,-1)
print(result)

#2

arr2 = np.arange(10)
result = arr2.reshape(2,5)
print(result)

#3

arr3 = np.array([1,2,3])
result = np.r_[np.repeat(arr3,3),np.tile(arr3,3)]
print(result)

#4

a4 = np.array([1,2,3,2,3,4,3,4,5,6])
b4 = np.array([7,2,10,2,7,4,9,4,9,8])
result = np.intersect1d(a4,b4)
print(result)

#5

a5 = np.array([1,2,3,2,3,4,3,4,5,6])
b5 = np.array([7,2,10,2,7,4,9,4,9,10])
result = np.where(a5 == b5)
print(result)

#6

result = np.random.uniform(low=5,high=10,size=(5,3))
print(result)


#7

arr7 = np.arange(15)
np.set_printoptions(threshold=5)
print(arr7)
#8

np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
np.set_printoptions(precision=6,suppress=True)
print(rand_arr)

#9

arr9 = np.arange(9).reshape(3,3)
# print(arr9)

col1 = 0
col2 = 1
arr9.T[[col1, col2]] = arr9.T[[col2, col1]]
print(arr9)

#10

row1 = 0
row2 = 1
arr10 = np.arange(9).reshape(3,3)
# print(arr10)
arr10[[row1,row2]] = arr10[[row2,row1]]
print(arr10)
