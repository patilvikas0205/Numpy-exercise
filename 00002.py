import numpy as np
import sys
'''
Creating Numpy array using list
'''
print("Creating array Using list")
list=[1,2,3,4,5]
arr1=np.array(list)
#arr1=np.array([1,2,3,4,5])
print("Numpy array is: ",arr1)
print("Lets check the type of object aar1 is: ",type(arr1))
print("Lets check id of arr1: ",id(arr1))
print("Lets check size of array object: ",sys.getsizeof(arr1))
print("Lets check dimension of arr1: ",arr1.ndim)
print("Check shape of arra1: Return in tuple ",arr1.shape)
print("check size (no of elements) of arr1: ",arr1.size)
print("Accessing Elemnets from arr1 array objects: ")
print("print oth element: ",arr1[0],arr1[1],arr1[2])
print("find number of rows and columns in arr1 array using shape :")
m=arr1.shape
print("Rows: ",m)
print("Loop through the array arr1: ")
for i in arr1:
    print(i,end=" ")

print("\nLoop through the array arr1: ")
for i in range(len(arr1)):
    print(arr1[i],end=" ")

print("Whether array object mutable")
print("array object before change :",arr1)
print("check id of arr1: ",id(arr1))
arr1[2]=200
print("After change arr1[2]=200",arr1)
print("check id of arr1: ",id(arr1))
print("Ids of both are same so its mutable")


