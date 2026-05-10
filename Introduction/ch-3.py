#Indexing and Slicing
#Indexing
import numpy as np
arr_1=np.array([10,20,30,40,50])
print(arr_1[0])
print(arr_1[3])
print(arr_1[4])
#Slicing
import numpy as np
arr_2=np.array([10,20,30,40,50])
print(arr_2[2::])
print(arr_2[:2])
print(arr_2[::2])
print(arr_2[::-1])
print(arr_2[1:2:])
#Fancy Indexing
import numpy as np
arr_3=np.array([10,20,30,40,50])
print(arr_3[[1,3]])
#Boolean Masking(Filtering)
import numpy as np
arr_4=np.array([10,20,30,40,50])
print(arr_4[arr_4 <20])
print(arr_4[arr_4 >20])
#Reshaping and Manipulating in Array(we are change the rows and column by reshaping not elements)
import numpy as np
arr_5=np.array([1,2,3,4,5,6])
print(arr_5.reshape(2,3))
#Ravel and Flatter (we are using for convert any type of aray in 1D array)
import numpy as np
arr_6=np.array([[1,2,3],
                [4,5,6]])
print(arr_6.flatten())
print(arr_6.ravel())


