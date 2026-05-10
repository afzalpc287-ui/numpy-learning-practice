#trial program
import numpy as np
tempreture = np.array([32.5,31.8,33.0,35.2,36.6])
average=np.mean(tempreture)
print(average)
#Arrays(How many types of array)
#1. 1D Array-One Dimentional Array
import numpy as np
array_1d=np.array([1,2,3,4,])
print(array_1d)
#2.2D Array -Two Dimentional Array
import numpy as np
array_2d=np.array([[1,2,3,4],
                   [5,6,7,8]])
print(array_2d)
#3. Multi-Dimentional Array (Matrix)
import numpy as np
multi_array=np.array([[1,2,3,4],
                      [5,6,7,8]])
print(multi_array)
# difference between python list and numpy array
#python list
python_list=[1,2,3,4,5,6,7,8,9,10]
print(python_list)
#numpy array
import numpy as np 
array=np.array([1,2,3,4,5,6,7,8,9,10])
print(array)
#Creating Arrays
#Create Numpy Array from Python List
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
#Print full of zero array
import numpy as np
arr_zero=np.zeros(2)
print(arr_zero)
#Print full of one array
import numpy as np
arr_ones=np.ones((2,3))
print(arr_ones)
#Print filled array
import numpy as np
filled_array=np.full((2,3),7)
print(filled_array)
#Print sequence array
import numpy as np 
seq_array=np.arange(2,10,2)
print(seq_array)
#Print identity matrix
import numpy as np
iden_array=np.eye(2,3)
print(iden_array)