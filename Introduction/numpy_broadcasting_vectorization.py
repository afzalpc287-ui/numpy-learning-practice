#Broadcasting
import numpy as np
price=np.array([100,200,300])
discount=10
final_price=price-(price*discount/100 )
print(final_price)
#Matching Dimentions
import numpy as np 
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
result=arr1+arr2
print(result)
#Matching Dimention in 2D Array
import numpy as np
arr2d1=np.array([[1,2,3],[4,5,6]])
arr2d2=np.array([[4,5,6],[3,2,1]])
result=arr2d1+arr2d2
print(result)
#Single Expend Element
import numpy as np
arr_s1=np.array([4,5,6])
result=arr_s1*2
print(result)
#Single Expend Element in 2D
import numpy as np
arr_s2=np.array([[4,5,6],[7,8,9]])
result=arr_s2*2
print(result)
#Vectorization
#Adding two arrays
import numpy as np
arr_v1=([10,20,30])
arr_v2=([40,50,60])
addition=arr_v1+arr_v2
print(addition)
#In 2D Array
import numpy as np
arr_v2d1=([[10,20,30],[40,50,60]])
arr_v2d2=([[70,80,90],[20,40,60]])
result=arr_v2d1+arr_v2d2
print(result)
#Multiplication
import numpy as np
arr_m=np.array([10,20,30])
multipleid=arr_m*3
print(multipleid)
#In 2D
arr_m2d=np.array([[10,20,30],[40,50,60]])
multipleid=arr_m2d*2
print(multipleid)