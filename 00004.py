import numpy as np
'''
datatype of array
'''
print("Creating array using arange()")
arr1=np.arange(1,10,1)
print("Array is:\n ",arr1)
print("check default data type of this array oject: ",arr1.dtype)
print("Depending on operating systems bit")
print("####################################################")
print("Chenge data type of array int32 to float explicitely: ")
arr1_float=np.arange(1,10,1,dtype=np.float)
print("after changing data type: ",arr1_float,"and type",arr1_float.dtype)
print("####################################################")
print("Combine int and float, int char and check datatype")
list1=[1,2,3.4,"ABC"]
arr2=np.array(list1)
print("Array is : ",arr2)
print("Check data type:  ",arr2.dtype)
print("###########################################################")
print("Combine int and float, int char and check datatype")
list1=[1,2,3.4]
arr2=np.array(list1)
print("Array is : ",arr2)
print("Check data type . means float value:  ",arr2.dtype)
print("###########################################################")
print("Explicitely change int to string")
list1=[1,2,3]
arr2=np.array(list1)
print("Array is : ",arr2)
print("Check data type:  ",arr2.dtype)
arr2=np.array(list1,dtype=np.str)
print("after int to str",arr2)
print("Check data type after to str:  ",arr2.dtype)
print("##################################")
print("this way you can change one datatypes explicitely to any other data type")