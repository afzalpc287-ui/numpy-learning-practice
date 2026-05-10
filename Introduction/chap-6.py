#Handling Missing and Special Values
#NAN(Not A Number)
import numpy as np
arr=np.array([1,2,np.nan,4,5,np.nan])
print(np.isnan(arr))
#No
print(np.nan==np.nan)
#isinf(INFINITE)
import numpy as np
arr1=np.array([1,2,np.inf,4,-np.inf,6])
print(np.isinf(arr1))
#NAN to NUM
import numpy as np
arr2=np.array([1,2,np.nan,4,5,np.nan])
arr3=np.array([1,2,np.inf,4,-np.inf,6])
print(np.nan_to_num(arr2,nan=7))
print(np.nan_to_num(arr3,posinf=10,neginf=20))

