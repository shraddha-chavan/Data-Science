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
