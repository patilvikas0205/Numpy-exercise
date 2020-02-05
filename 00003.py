import numpy as np
'''
creating array using arange()
arange(start,stop,step)
'''
arr1=np.arange(1,10,1)
print("Array is ",arr1)
print("Check type: ",type(arr1))
print("id of array object",id(arr1))
print("Size of arr1: ",arr1.size)
print("check dimension: ",arr1.ndim)
print("check shape of arr1: ",arr1.shape)

print("Convert into two dimension using reshape()")
print("After Reshaping: ",arr1)
arr1=arr1.reshape(3,3)
print("After Reshaping:")
print(arr1)
print("Dimension after reshape: ",arr1.ndim)
print("check shape after reshape (in tuple): ",arr1.shape)
print("No of rows and columns in arr1")
m,n=arr1.shape
print("rows : ",m,"cols :",n)
print("Access element of two dimension array: ")
print(arr1[1],"return entire list as first element")
print("accessing 1st row and 2 colummn element")
print(arr1[1][2])

print("loop through two d array")
print("Elements: ")
for i in arr1:
    print(i,end="")

print("\nloop through two d array")
print("Elements in ith row ang jth col: ")
for i in range(len(arr1)):
    for j in range(len(arr1)):
        print(arr1[i][j],end=" ")

print("\narray to list use tolist()")
print("Ariginal array is")
print(arr1)
print("array to list")
print(arr1.tolist())