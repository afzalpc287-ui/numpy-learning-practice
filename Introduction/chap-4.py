#Reshaping and manipulating in Arrays
# How to insert the elements on a specific index in  Array
"""np.insert(arr,ind,val,axis)
axis=0 so the data is inserting in row
axis=1 so the data is inserting in colunm
axis=none so the data is inerting in flatten"""
import numpy as np
arr_1=np.array([1,2,3,4,5])
print(arr_1)
new_arr1=np.insert(arr_1,2,100,axis=0)
print(new_arr1)
#in 2d array
import numpy as np
arr_1_2=np.array([[1,2,3],[4,5,6]])
print(arr_1_2)
new_arr1_2=np.insert(arr_1_2,1,[7,8,9],axis=0)
print(new_arr1_2)
#How to add the elements in the last of array
"""np.append(arr,value,axis)"""
import numpy as np
arr_2=np.array([1,2,3,4])
print(arr_2)
new_arr2=np.append(arr_2,[5,6,7,8],axis=0)
print(new_arr2)
#in 2d array
import numpy as np
arr_2_2=np.array([[1,2,3],[4,5,6]])
print(arr_2_2)
new_arr2_2=np.append(arr_2_2,[7,8,9],axis=None)
print(new_arr2_2)
#How to add and continent of two arrays
"""np.continet(arr1,arr2)"""
import numpy as np
arr_con1=np.array([1,2,3])
arr_con2=np.array([4,5,6])
new_arr_con=np.concatenate((arr_con1,arr_con2))
print(new_arr_con)
#in 2d array
import numpy as np
arr_con_2d1=np.array([[1,2,3],[4,5,6]])
arr_con_2d2=np.array([[4,5,6],[1,2,3]])
new_con_2d=np.concatenate((arr_con_2d1,arr_con_2d2))
print(new_con_2d)
#How to delete the elements from a specific index in array
"""np.delete(arr,ind,axis)"""
import numpy as np
arr_3=np.array([1,2,3,4,5,6,7,8,9])
print(arr_3)
new_arr3=np.delete(arr_3,3,axis=0)
print(new_arr3)
#in 2d array
import numpy as np
arr_2d_3=np.array([[1,2,3],[4,5,6]])
print(arr_2d_3)
new_arr3_2d=np.delete(arr_2d_3,1,axis=1)
print(new_arr3_2d)
#Stacking in arrays 
"""np.vstack(row wise) = verticle like 2d array
np.hstack (colunm wise)= horizontal like 1d array"""
import numpy as np
arr_4a=np.array([1,2,3])
arr_4b=np.array([4,5,6])
new_arr4=np.stack((arr_4a,arr_4b))
print(new_arr4)
new_arr4v=np.vstack((arr_4a,arr_4b))
print(new_arr4v)
new_arr4h=np.hstack((arr_4a,arr_4b))
print(new_arr4h)
#How to split the array in parts
import numpy as np
arr_5=np.array([1,2,3,4,5,6,7,8,9])
print(arr_5)
new_arr5=np.split(arr_5,3)
print(new_arr5)
#in 2d array
import numpy as np
arr_5_2d=np.array([[1,2,3],[4,5,6]])
print(arr_5_2d)
new_arr5_2d=np.split(arr_5_2d,2)
print(new_arr5_2d)