# ------------------------------------------------------------------------ 1. NumPy Introduction ------------------------------------------------------------------------



# What is NumPy?

"""

NumPy is a short name for "Numerical Python".
NumPy is python library.
NumPy is used for working with arrays.

"""

# Why NumPy?

"""
In python we have a "List" that serves the purpose of array, but it is very slow to process.
So List has alternative of NumPy that is 50x faster than List.

"""

# Why NumPy is faster than List?

"""
NumPy stores data elements in Contiguous manner. That means, the data elements are stored adjacent to each other or one continuous place in memory. Whereas, List stores data elements in scattered manner.


"""





# ------------------------------------------------------------------------ 2. Checking NumPy Version ------------------------------------------------------------------------


import numpy as np

print(np.__version__)



# ------------------------------------------------------------------------ 3. Creating NumPy arrays ------------------------------------------------------------------------



"""
The array object in NumPy called as ndarray.
We can create NumPy ndarray object using array() function.

""" 

import numpy as np 

data = np.array([1, 2, 3])
print(data)
print(type(data))



### ------------------------------------------------------------------------ 3.1. Passing python List to Numpy array ------------------------------------------------------------------------


import numpy as np

list1 = [1, 2, "Tejas"]
arr = np.array(list1)
print(arr)


### ------------------------------------------------------------------------ 3.2 Passing python tuple to Numpy array ------------------------------------------------------------------------



import numpy as np

arr = np.array((1, 2, "Tejas"))
print(arr)


### ------------------------------------------------------------------------ 3.3. Passing python dictionary to NumPy array ------------------------------------------------------------------------


import numpy as np

arr = np.array({'name' : 1, 'email' : 2})
print(arr)





# ------------------------------------------------------------------------ 4. Dimension in arrays ------------------------------------------------------------------------

## ------------------------------------------------------------------------ 4.1. 0-D array (0 Dimension array) ------------------------------------------------------------------------


import numpy as np

arr = np.array(42)
print(arr)





## ------------------------------------------------------------------------ 4.2. 1-D array (1 Dimension array) ------------------------------------------------------------------------ 



import numpy as np 

arr = np.array([12, 24, 36])
print(arr)


## ------------------------------------------------------------------------ 4.3. 2-D array (2 Dimension array) ------------------------------------------------------------------------


import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)


# ------------------------------------------------------------------------ 4.4. 3-D array (3 Dimension array) ------------------------------------------------------------------------



import numpy as np 

arr = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
print(arr)


### Checking number of Dimensions: - 


import numpy as np 

zero_dim = np.array(42)
one_dim = np.array([1,2,3])
two_dim = np.array([[1,2,3],[4,5,6]])
three_dim = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])

print(zero_dim.ndim, "-dimensional array")
print(one_dim.ndim, "-dimensional array")
print(two_dim.ndim,  "-dimensional array")
print(three_dim.ndim,  "-dimensional array")


### Higher Dimension arrays: - 


"""
An array can have any number of dimensions.
When the array is created you can define number of dimensions by using "ndmin" argument.

""" 


import numpy as np

arr = np.array([1, 2, 3], ndmin = 5)
print(arr)
print("Number of dimensions are: - ", arr.ndim)


"""
In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector,
the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.

""" 





# ------------------------------------------------------------------------ 5. NumPy Array Indexing ------------------------------------------------------------------------




"""
Array indexing is same as accessing array element.
You can access array element by referring to its index number.
The indexes starts with 0, meaning that first element has index 0, and second has index 1.

""" 


import numpy as np

arr = np.array([12, 21, 30, 41])
print(arr)
print("The first index element is: - ", arr[0])




# Addition of 3rd and 4th array elements: - 

import numpy as np

arr = np.array([12, 21, 30, 41, 59])
print(arr)
print("The addition of 3rd and 4th element is: - ", arr[3] + arr[4])





## ------------------------------------------------------------------------ 5.1. Accessing 2-D array: - ------------------------------------------------------------------------




"""
To access element from 2-D array. we can use comma separated integers representing dimension, and index of element.

""" 

import numpy as np

arr = np.array([[1,2,3], [4,5,6]])
print(arr)
print(arr[0,2])                         # Here we are accessing element from 0th dimension and 2nd index element.



## ------------------------------------------------------------------------ 5.2. Accessing 3-D array: - ------------------------------------------------------------------------





"""
To access element from 3-D array. we can use comma separated integers representing 1st dimension, 2nd dimension, and index of element.

""" 

import numpy as np

arr = np.array([[[1,2,3], [4,5,6]], [[7,8,9],[10,11,12]]])
print(arr)
print(arr[0,1,2])                          # Here we are accessing element from 0th dimension, 1st dimension and 2nd index element.



"""

Example Explained
arr[0, 1, 2] prints the value 6.

And this is why:

The first number represents the first dimension, which contains two arrays:
[[1, 2, 3], [4, 5, 6]]
and:
[[7, 8, 9], [10, 11, 12]]
Since we selected 0, we are left with the first array:
[[1, 2, 3], [4, 5, 6]]

The second number represents the second dimension, which also contains two arrays:
[1, 2, 3]
and:
[4, 5, 6]
Since we selected 1, we are left with the second array:
[4, 5, 6]

The third number represents the third dimension, which contains three values:
4
5
6
Since we selected 2, we end up with the third value:
6


""" 




## ------------------------------------------------------------------------ 5.3. Negative Indexing: - ------------------------------------------------------------------------



# To access last element we can simply say arr[-1].

import numpy as np

arr = np.array([1,2,3])
print(arr[-1])




# ------------------------------------------------------------------------ 6. NumPy Array Slicing ------------------------------------------------------------------------


"""
Slicing in python means taking elements from one given index to another given index.
We can specify it by: - [start:end].
We can also specify: - [start:end:step].
If we don't pass start index then, it by default starts with 0th index.     e.g.-> [:3]
If we don't pass end index then, it considers length of an array.         e.g.-> [0:]
And if we don't pass step then, it considers 1.                            

""" 


import numpy as np 

arr = np.array([10, 20, 30, 40, 50])


print(arr[1:3])
print(arr[:4])
print(arr[1:])
print(arr[0::2])        # Here we haven't specified end index so, it will consider till last index element, and step as 2.



## ------------------------------------------------------------------------ 6.1. Negative Slicing: - ------------------------------------------------------------------------



import numpy as np 

arr = np.array([10, 20, 30, 40, 50])

print(arr[-3:-1])                       # remember last element is considers as -1



## ------------------------------------------------------------------------ 6.2. Slicing 2-D arrays: - ------------------------------------------------------------------------



import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr)
print(arr[1, 1:4])                     # Here we are getting elements from 1st dimension, from 1st index to 3rd as last index is not considered in python.


print("---------------------------------------------------------------------------------------------------------------------------------------------------------")


# If you want to get the 1st index element from both the dimensions 0th and 1st then: - 

import numpy as np


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print("If you want to get the 1st index element from both the dimensions 0th and 1st then: -") 
print(arr[0:2, 1])




print("---------------------------------------------------------------------------------------------------------------------------------------------------------")


# If you want to get the 1st to 4th index(not included) element from both the dimensions 0th and 1st then: -



import numpy as np


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print("If you want to get the 1st to 4th index(not included) element from both the dimensions 0th and 1st then: -") 
print(arr[0:2, 1:4])








# ------------------------------------------------------------------------ 7. NumPy Data Types ------------------------------------------------------------------------




# By default Python has following data types: - 

"""
1) string   2) integer  3) float    4) double   5) boolean  6) complex

"""

# Data types in NumPy: - 

"""
Numpy has extra data types and refer to data types with one character, like 'i' for integer, 'u' for unsigned integer, etc.
Following is the list of all data types in NumPy: -

i - integer
b - boolean
u - unsigned integer
f - float
c - complex data
m - timedelta
M - datetime
O - object
S - String
U - Unicode String
V - Fixed chunk of memory for other data type (void)

"""





### ------------------------------------------------------------------------ 7.1. Checking the Data Type of an Array: -  ------------------------------------------------------------------------




# We can check datatype of an array by "array.dtype" property.


# EXAMPLE 1: - 


import numpy as np

arr = np.array([1,2,3])

print(arr)
print(arr.dtype)

print("---------------------------------------------------------------------------------------------------------------------------------")

# EXAMPLE 2: - 


import numpy as np

arr = np.array(['a','b','c'])

print(arr)
print(arr.dtype)




### ------------------------------------------------------------------------ 7.2. Creating an array with defined Data Type: - -------------------------------------------------------------------





import numpy as np

arr = np.array([1,2,3,4], dtype='S')

print(arr)
print(arr.dtype)



# For i, u, f, S, and U we can define size as well.

import numpy as np

arr = np.array([1,2,3,4], dtype='i4')

print(arr)
print(arr.dtype)




### ------------------------------------------------------------------------ 7.3. What if value cannot be converted? ------------------------------------------------------------------------



# If a type is given in which element can't be casted then NumPy will raise a Valueerror.

# ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.

import numpy as np

arr = np.array(['a', 2, 3], dtype = 'i')            # This will give you an error as you are trying to convert 'a' element to integer.







### ------------------------------------------------------------------------ 7.3.1 Converting Data type on Existing array: - -------------------------------------------------------------------



"""
- Best way to change the data type of an existing array is to make a copy of an array with astype() method.
- astype() method creates a copy of the array, and allows you to specify the data type as a parameter.
- You can specify the data type by 'i' for integers, 'f' for float, etc.  OR you can specify it by data type directly like float for float, int for integer.

""" 


# EXAMPLE 1): - 


import numpy as np

arr = np.array([1,2,3,4])
new_arr = arr.astype('S')

print(new_arr)
print(new_arr.dtype)

print("--------------------------------------------------------------------------------------------------------------------")


# EXAMPLE 2): - 


import numpy as np

arr = np.array([1.1, 2.1, 3.1])
new_arr = arr.astype('i')
print(new_arr)
print(new_arr.dtype)

print("--------------------------------------------------------------------------------------------------------------------")

# EXAMPLE 3): - 


import numpy as np

arr = np.array([1.1, 0.0, 3.1])
new_arr = arr.astype(bool)
print(new_arr)
print(new_arr.dtype)





# ------------------------------------------------------------------------ 8. NumPy Copy vs View ------------------------------------------------------------------------



"""
- The main difference between "copy" and "view" is that, "copy" is a new array, and the "view" is just a view of the original array.
- "copy" owns the data and changes made to original array will not affect the copy, and changes made to copy will not affect the original array.
- "view" does not own the data and changes made to the original array will affect the view, and changes made to the view will affect the original array.

""" 




### ------------------------------------------------------------------------ 8.1. Numpy COPY: - ------------------------------------------------------------------------





import numpy as np 

arr = np.array([1,2,3,4])

x = arr.copy()
print(x)
print(arr)




### ------------------------------------------------------------------------ 8.1.1 Making changes to COPY array / Making changes to original array: - ----------------------------------------




# If we made changes to copy, it will affect original And if we made changes to original, it will affect copy.

import numpy as np

arr = np.array([1,2,3,4])
x = arr.copy()

x[2] = 30
print(arr)
print(x)




### 8.2. Numpy VIEW: - 



import numpy as np

arr = np.array([1,2,3,4])

x = arr.view()
print(x)
print(arr)



### ------------------------------------------------------------------------ 8.2.1. Making changes to VIEW array / Making changes to original array: - -------------------------------------




# If we made changes to view, it will affect original And if we made changes to original, it will affect view.

import numpy as np 

arr = np.array([1,2,3,4])

x= arr.view()
x[1] = 20
print(x)
print(arr)






## ------------------------------------------------------------------------ 8.3. Check if array owns its data: - ------------------------------------------------------------------------




# As we know copy owns the data, and view does not. But how can we check it?

# Every NumPy array has attribute "base" that returns 'None' if the array owns the data. Otherwise "base" attribute refers to original object.

import numpy as np

arr = np.array([1,2,3,4])
x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)





# ------------------------------------------------------------------------ 9. NumPy Array Shape ------------------------------------------------------------------------



"""
- The shape attribute of a NumPy array returns a tuple representing the dimensions of the array. 
- In following example, "arr.shape" will return a tuple - (2, 4), indicating that arr is a 2-dimensional array with 2 rows and 4 columns.

"""


# Example 1): - 

import numpy as np

arr = np.array([[1,2,3,4], [5,6,7,8]])
print(arr)
print(arr.shape)            # O/P: - (2,4) i.e. 2 dimensions and 4 columns





# Example 2): - 



import numpy as np


arr = np.array([1,2,3,4], ndmin=5)        # Here we created an array with 5 dimensions.
print(arr)
print(arr.shape)            # o/p: - (1,1,1,1,4)






# ------------------------------------------------------------------------ 10. NumPy Array Reshaping ------------------------------------------------------------------------




# Reshaping means changing the shape of an array.



print(" -------------------------------------------------------------------- RESHAPING FROM 1-D to 2-D: - ---------------------------------------------------------------------")
# RESHAPING FROM 1-D to 2-D: - 

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr = arr.reshape(4,3)
print(new_arr)


print(" -------------------------------------------------------------------- RESHAPING FROM 1-D to 3-D: - ---------------------------------------------------------------------")
# RESHAPING FROM 1-D to 3-D: - 

import numpy as np 

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_arr = arr.reshape(2,2,3)
print(new_arr)


# Note: - we can shape into any shape, as long as the elements required for reshaping are equal in both shapes.
# Following example will raise an error as it cannot shape the 8 elements array into 3 rows and 3 columns. 

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(3, 3)





### ------------------------------------------------------------------------ 10.1. Check if the returned array is a copy or a view: -------------------------------------------------------





import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)           # The example above returns the original array, so it is a view.




### ------------------------------------------------------------------------ 10.2. Unknown Dimensions: - ------------------------------------------------------------------------



"""

You are allowed to have one "unknown" dimension.
Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
Pass -1 as the value, and NumPy will calculate this number for you.

""" 

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

# Note: We can not pass -1 to more than one dimension.





### ------------------------------------------------------------------------ 10.3. Flattening the arrays: - ------------------------------------------------------------------------




# We can use reshape(-1) to do this.

import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
new_arr = arr.reshape(-1)
print(arr)
print(new_arr)




# ------------------------------------------------------------------------ 11. NumPy Array Iterating ------------------------------------------------------------------------


# Iterating through array means going through array one by one. We can do it using basic "for" loop of python.
# If we iterate on a 1-D array it will go through each element one by one.





### ------------------------------------------------------------------------ 11.1. Iterating through 1-D array: - ------------------------------------------------------------------------



print("------------------------------------------------------------- Iterating through 1-D array ---------------------------------------------------------------------------")

import numpy as np

arr = np.array([1,2,3,4])

for x in arr:
    print(x) 





### ------------------------------------------------------------------------ 11.2. Iterating through 2-D array: - ------------------------------------------------------------------------




print("------------------------------------------------------------- Iterating through 2-D array ---------------------------------------------------------------------------")


import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])

for x in arr:
    print(x)


# If we want actual values or scalar values then: - 
print("----------------------------------------------------------------------------------------------------------------")
    

import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])

for x in arr:
    for y in x:
        print(y)





### ------------------------------------------------------------------------ 11.3. Iterating through 3-D array: - ------------------------------------------------------------------------



print("------------------------------------------------------------- Iterating through 3-D array ---------------------------------------------------------------------------")


import numpy as np

arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

for x in arr:
    print(x)


# To return actual values, the scalar values: - 
    
print("----------------------------------------------------------------------------------------------------------------")


import numpy as np

arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

for x in arr:
    for y in x:
        for z in y:
            print(z)






### ------------------------------------------------------------------------ 11.4. Iterating arrays Using nditer(): -------------------------------------------------------------------------




# nditer() is a helping function that can be used from very basic to very advanced iterations. It solve some basic issues which we face in iteration.

import numpy as np

arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

for x in np.nditer(arr):
    print(x)



### ------------------------------------------------------------------------ 11.5. Iterating Array With Different Data Types ---------------------------------------------------------------




# We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.

# NumPy does not change the data type of the element in-place (where the element is in array) 
# so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].


import numpy as np

arr = np.array([1,2,3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)




# ------------------------------------------------------------------------ 12. NumPy Array Join ------------------------------------------------------------------------






# In SQL we join tables based on a key, whereas in NumPy we join arrays by axis.
# We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.


import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

new_arr = np.concatenate((arr1, arr2))
print(new_arr)





### ------------------------------------------------------------------------ 12.1. Join two 2-D arrays along rows (axis=1):---------------------------------------------------------------




import numpy as np

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

new_arr = np.concatenate((arr1, arr2), axis=1)
print(new_arr)






### ------------------------------------------------------------------------ 12.2. Joining Arrays Using Stack Functions: - ------------------------------------------------------------------------





import numpy as np


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)






### ------------------------------------------------------------------------ 12.3. Stacking Along Rows: - ------------------------------------------------------------------------



# NumPy provides a helper function: hstack() to stack along rows.

import numpy as np


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

new_arr = np.hstack((arr1,arr2))
print(new_arr)






### ------------------------------------------------------------------------ 12.4. Stacking Along Columns: - ------------------------------------------------------------------------



# NumPy provides a helper function: vstack() to stack along Columns.

import numpy as np


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

new_arr = np.vstack((arr1,arr2))
print(new_arr)





### ------------------------------------------------------------------------ 12.5. Stacking Along Height (depth): - ------------------------------------------------------------------------



import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)





# ------------------------------------------------------------------------ 13. NumPy Splitting Array: - ------------------------------------------------------------------------



# Splitting is a reverse process of joining.
# Joining merges multiple arrays into one, whereas splitting breaks one array into multiple.

"""
There are 2 methods: -  array_split(): - If the array has less elements than required, it will adjust from the end accordingly.
                        split(): -      This method gives error when the array has less elements than required. 

"""


import numpy as np

arr = np.array([1,2,3,4,5,6])
new_arr = np.array_split(arr, 3)
print(new_arr)


# Note: We also have the method split() available but it will not adjust the elements when elements are less in source array for splitting like in example above.





### ------------------------------------------------------------------------ 13.1. Split into Arrays: - ------------------------------------------------------------------------




import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])




### ------------------------------------------------------------------------ 13.2. Splitting 2-D Arrays: - ------------------------------------------------------------------------





# Split the 2-D array into three 2-D arrays.

import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)


print("------------------------------- Splitting 2-D array into 3 2-D array: - ----------------------------------------------------------------------")

# EXAMPLE 2): - Splitting 2-D array into 3 2-D array: - 

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)







### ------------------------------------------------------------------------ 13.3. Splitting 2-D arrays with axis: - ------------------------------------------------------------------------





import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)





# ------------------------------------------------------------------------ 14. NumPy Searching Arrays: - ------------------------------------------------------------------------



# You can search an element from an array and return an index of that element by "where()" method.

import numpy as np 


arr = np.array([3,4,5,6])
x = np.where(arr == 4)
print(x)




# EXAMPLE 2): - 

import numpy as np 


arr = np.array([1,2,3,3,4,5,6,3])
x = np.where(arr == 3)
print(x)




# EXAMPLE 3) Find indexes of even elements: - 

import numpy as np 

arr = np.array([1,2,3,4,5,6])
x = np.where(arr % 2 == 0)
print(x)



# EXAMPLE 4) Find indexes of odd elements: - 

import numpy as np 

arr = np.array([1,2,3,4,5,6])
x = np.where(arr % 2 == 1)
print(x)





### ------------------------------------------------------------------------ 14.2. searchsorted() method: - ------------------------------------------------------------------------



# searchsorted() method performs binary search in the array, and returns the index position where specified element should be inserted to maintain the search order.
# Always pass the sorted array otherwise it will not behave properly.

import numpy as np

arr = np.array([3,5,6,9])
x = np.searchsorted(arr, 7)
print(x)



"""

- If you want to search from right side simply give " side = 'right' ".
- By default, side='left' means the function will return the leftmost (i.e., the lowest) index where the value could be inserted without changing the order of the array.
- side='right' means the function will return the rightmost (i.e., the highest) index where the value could be inserted.


""" 
    

import numpy as np 

arr = np.array([3,5,6,7,9])
x = np.searchsorted(arr, 7, side = 'right')
print(x)








### ------------------------------------------------------------------------ 14.3. Multiple Values: - ------------------------------------------------------------------------




# To search more than 1 value, use an array with specified values.

import numpy as np

arr = np.array([1, 5, 7, 10, 11, 14, 20])
x = np.searchsorted(arr, [7, 11, 20])
print(x)







# ------------------------------------------------------------------------ 15. Numpy Sorting Arrays ------------------------------------------------------------------------




"""

- Sorting means putting arrays in an ordered sequence.
- Numpy ndarray object has a function called sort(), that will sort a specified array.
- sort() will return a copy of ordered array, leaving the original array unchanged. 

"""

# EXAMPLE 1): - Sorting Numerical elements: - 
print("------------------------------- Sorting Numerical elements : - ----------------------------------------------------------------------")


import numpy as np 

arr = np.array([3, 2, 1, 0])
x = np.sort(arr)
print(x)


# EXAMPLE 2): - Sorting alphabetical elements: - 
print("------------------------------- Sorting Alphabetical elements : - ----------------------------------------------------------------------")


import numpy as np 


arr = np.array(['banana', 'apple', 'cherry'])
x = np.sort(arr)
print(x)



# EXAMPLE 3): - Sorting boolean elements: - 
print("------------------------------- Sorting boolean elements : - ----------------------------------------------------------------------")


import numpy as np 


arr = np.array([True, False, True])
x = np.sort(arr)
print(x)






### ------------------------------------------------------------------------ 15.1. Sorting 2-D array: - ------------------------------------------------------------------------





# If you use sort() on both 2-D array, it will sort both the array.

import numpy as np 

arr = np.array([4, 3, 8, 6, 7])
x = np.sort(arr)
print(x)





# ------------------------------------------------------------------------ 16. Numpy Filter Array ------------------------------------------------------------------------





# Getting some elements out of existing array and creating a new array out of them is called as "Filtering".
# In Numpy, we use boolean index list to filter an array. 
# If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.

import numpy as np 


arr = np.array([12, 54, 45, 78])
filter_array = [True, False, True, False]
new_array = arr[filter_array]

print(new_array)

# New array contains only the values where the filter array had the value True. In this case index 0 and 2.







### ------------------------------------------------------------------------ 16.1. Creating filter array based on conditions: - ----------------------------------------------------------------




# Condition: - get the elements greater than 50.

import numpy as np 


filter_array = []

arr = np.array([10, 20, 30, 54, 89, 65])
for element in arr:
    if element > 50:
        filter_array.append(True)
    else: 
        filter_array.append(False)

new_arr = arr[filter_array]
print(new_arr)
        





# Condition: - get the even elements from an array.


import numpy as np 

filter_array = []

arr = np.array([12, 56, 78, 94, 55])
for element in arr:
    if element % 2 == 0:
        filter_array.append(True)
    else:
        filter_array.append(False)
    
new_arr = arr[filter_array]
print(new_arr)






### ------------------------------------------------------------------------ 16.2. Creating Filter directly from Array: - --------------------------------------------------------------------




# The above example is quite a common task in NumPy and NumPy provides a nice way to tackle it.
# We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.

import numpy as np 

arr = np.array([41, 42, 43, 44])
filter_array = arr > 42

print(filter_array)
print(arr[filter_array])




# Condition: - Getting even elements from an array.


import numpy as np 

arr = np.array([12, 56, 78, 94, 55])
filter_array = (arr % 2 == 0)

print(filter_array)
print(arr[filter_array])





































