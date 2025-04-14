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


#create 9 random number from 1,9
arr=np.random.randint(1,100,9)
arr
#find square (arr)
np.sqrt(arr)
#find sin of array
np.sin(arr)
#find exponential
np.exp(arr)
#find log
np.log(arr)
#find meand
np.mean(arr)
#find median
np.median(arr)
##########################################

#find that in how many percentile number exists
#i.e:Q1,Q2,Q3 == 25%,50%,75%
arr1=np.array([10,20,30,40,50,60,70])
arr1
arr1.mean()
np.percentile(arr1,25)
np.percentile(arr1,50)
np.percentile(arr1,75)
 
#create a 2d numpy array
import numpy as np
import matplotlib.pyplot as plt
#consider the list a, the list contains three 
#nested 
#create a list
a=[[11,12,13],[21,22,23],[31,32,33]]                                               
a
#convert list to numpy array
#every element is the same type
A=np.array(a)
A
'''Out[34]: 
array([[11, 12, 13],
       [21, 22, 23],
       [31, 32, 33]])'''
#access the element second
# row and third column
A[1,2]

#access the element first
# row and first column
A[0,0]
#access the element first
# row and first and second column
A[0][0:2]
#access the element first and second
# row and third column
A[0:2,2]


#Basic operation
#create a numpy array x
x=np.array([[1,0],[0,1]])
x
##create a numpy array y
y=np.array([[2,1],[1,2]])
y
#add x and y
Z=x+y
Z
#multiply a array by a scalar 
#create a numpy array y
y=np.array([[2,1],[1,2]])
y
#multiply y with 2
#scalar mul
Z=2*y
Z
#multiply x with y
Z=x*y
Z
#with the numpy arrays A and B as follows:
#create a matrix A
A=np.array([[0,1,2],[1,0,1]])
A
#create a matrix B
B=np.array([[1,1],[1,1],[-1,1]])
B


#we use the numpy attribute T to calculate
# the transform matrix
C=np.array([[1,1],[2,2],[3,3]])
C
#get transposed of C
C.T
###############################################
#write a numpy program to get version
import numpy as np
print(np.__version__)
print(np.show_config())

#write a numpy program to test element-wise for 
#complex numbers,real numbers in a given 
#array. also test if a given no. is of a sclar type
#or not
import numpy as np
a=np.array([1+1j,1+0j,4.5,3,2,2j])
print("original array")
print(a)
print("checking for complex numbers:")
print(np.iscomplex(a))
print("checking for real numbers:")
print(np.isreal(a))
print("checking for scalar type")
print(np.isscalar(3))
print(np.isscalar([3.1]))

########################################
#write a numpy program to compute
#the multiplication of 2 matrixes
import numpy as np
p=[[1,0],[0,1]]
p=np.array(p)
q=[[1,2],[3,4]]
q=np.array(q)
res=np.dot(p,q)
res

#########################################
#outer product is hadamard product
res=np.outer(p,q)
res

###############################
#hadamard product
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[ 7,8]])
hadamard=a*b
print("hadamard product:\n",hadamard)
###################################
#usually works with 1D vectors
import numpy as np
x=np.array([1,2])
y=np.array([3,4,5])
outer=np.outer(x,y)
print("Outer Product:\n",outer)
########################################
#write numpy program to compute the cross product
import numpy as np
p=[[1,0],[0,1]]
p=np.array(p)
q=[[1,2],[3,4]]
q=np.array(q)
print("original matrix:")
print(p)
print(q)
result1=np.cross(p,q)
result2=np.cross(q,p)
print("cross product of the said two vectors(p,q)")
print(result1)
print("cross product of the said two vectors(q,p)")
print(result2)

##################################################
#write a numpy program to compute the determinant
import numpy as np
from numpy import linalg as LA
a=np.array([[1,0],[1,2]])
print("Original 2-d array")
print(a)
print("Determinant of the said 2-D array:")
print(np.linalg.det(a))


######################################################
#write a code that the eigenvalues and right eigenvectors
# of the given square
import numpy as np
m=np.mat("3 -2;1 0")
print("Original matrix:")
print("a\n",m)
w,v=np.linalg.eig(m)
print("Eigenvector of the said matrix",w)
print("Eigenvector of the said matrix",v)

########################################
#write a numpy code to compute the inverse 
#of the given 
import numpy as np
n=np.array([[1,2],[3,4]])
print("Original matrix:")
print(m)
result=np.linalg.inv(m)
print("Inverse of the said matrix:")
print(result)


####################################
#array operations:
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
add = a + b

# Element-wise multiplication
mul = a * b

# Dot product
dot = np.dot(a, b)

# Sum, mean, std
total = np.sum(a)
average = np.mean(a)
standard_deviation = np.std(a)


#write a numpy program to generate five random number
import numpy as np
x=np.random.normal(size=5)
x
#write numpy program to generate six number
y=np.random.randint(low=10,high=30,size=6)
y
############################################
#write a numpy program to create 
import numpy as np
x=np.random.random((3,3,3))
x
################################
#write a numpy program to create a 5 by 5 array
#and find the minimum and maximum values.
import numpy as np
x=np.random.random((5,5))
print('original matrix')
x
xmin ,xmax=x.min(), x.max()
print("minimum and maximum values:")
print(xmin,xmax)
###########################################
#write a numpy program to get the minimum and 
#maximum values of a given array along the second axis
import numpy as np
x=np.arange(4).reshape((2,2))
print('\n original array:')
x
print("\n maximum values along the second axis:")
print(np.amax(x,1))
#this finds the max value along axis 1
#i.e along rows
#each row is:
    #row 0-[0,1]-max=1
    #row 1-[2,3]-max=3
print('minimum values along the second axis:')
print(np.amin(x,1))
#this finds the minimum value along axis 1
#each row is:
    #row 0-[0,1]-min=0
    #row 1-[2,3]-min=2
    
##############################################
























































