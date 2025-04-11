#common function of numpy
import numpy as np
x=np.array([1,2,3])
x
################
np.all(x)
x=np.array([1,2,3,0])
np.all(x)
##################
x=np.array([1,0,0])
np.any(x)
###############
x=np.array([1,2,np.nan,np.inf])
x
################
np.isfinite(x)
################
np.isnan(x)
################
x=np.array([3,5])
y=np.array([2,5])
np.greater(x,y)
np.greater_equal(x,y)
#####################
array_2D=np.identity(3)
array_2D
#################
rand_No=np.random.normal(0,1,2)
rand_No
######################
a=np.arange(10,22)
a
a=np.arange(10,22)
a
################################
import numpy as np
lst=[1,2,3]
arr=np.array(lst)
arr.ndim
arr.shape
type(arr)
arr_two=np.array([[1,2,3],[3,4,5],[6,7,8]])

arr_two.ndim
arr_two.shape
mat=np.matrix([[1,2,3],[4,5,6],[7,8,9]])

mat.ndim
mat.shape
##############################

################################
import numpy as np
lst=[1,2,3]
arr=np.array(lst)
arr.ndim
arr.shape
type(arr)
arr_two=np.array([[1,2,3],[3,4,5],[6,7,8]])

arr_two.ndim
arr_two.shape
mat=np.matrix([[1,2,3],[4,5,6],[7,8,9]])

mat.ndim
mat.shape
##############################
arr=np.random.randint(1,100,9)
arr
arr.ndim
new_arr=arr.reshape(3,3)
new_arr.ndim
new_arr.ravel()#convert 1d to 2d
arr[2]
###################################
#Extracting elements from 2 to 5
arr[2:6]
new_arr
''' output: array([[57, 75, 20],
       [71, 17, 81],
       [62, 26, 40]])'''

#extracting 26,40 from above 
new_arr[2,1:3]
##extracting 57,62,20,40 from above 
new_arr[[0,2,0,2],[0,0,2,2]]#first give row numbers then give column






























