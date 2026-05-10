#How to check shape of Array
import numpy as np
arr=np.array([[1,2,3],
      [4,5,6]])
print(arr.shape)
#How to check no. of elements in Array (size of Array)
import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1.size)
#How to check no. of dimention of Array (which type of Array)
import numpy as np
arr_1d=np.array([1,2,3])
arr_2d=np.array([[1,2,3,],[4,5,6]])
arr_3d=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)
#How to check the data type of Array elements 
import numpy as np
arr2=np.array([1,2.5,3])
print(arr2.dtype)
#How to change the data type of elements in Array
import numpy as np
arr3=np.array([1.5,2.5,3.5])
print(arr3)
print(arr3.dtype)
int_arr3=arr3.astype(int)
print(int_arr3)
print(int_arr3.dtype)
#Mathematical Operations
#operators
import numpy as np
arr_op=np.array([10,20,30])
print(arr_op)
print(arr_op+5)
print(arr_op-5)
print(arr_op*2)
print(arr_op/2)
print(arr_op**2)
#Aggregation Functions
import numpy as np
arr_agg=np.array([10,20,30,40,50])
print(np.sum(arr_agg))
print(np.mean(arr_agg))
print(np.min(arr_agg))
print(np.max(arr_agg))
print(np.std(arr_agg))
print(np.var(arr_agg))