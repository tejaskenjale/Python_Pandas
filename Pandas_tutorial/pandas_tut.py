# ------------------------------------------------------------------------ PRINT PANDAS VERSION ---------------------------------------------------------------------------------------------


import pandas as pd

print(pd.__version__)


# ------------------------------------------------------------------------ READING CSV FILE ------------------------------------------------------------------------------------------------ 

# use to_string() to print the entire DataFrame

import pandas as pd1

df = pd1.read_csv("C:/Users/POOJA KENJALE/Desktop/industry.csv")
print(df.to_string())



# --------------------------------------------------------------------------------------- READING EXCEL FILE ----------------------------------------------------------------------------------- 


import pandas as pd1
df = pd1.read_excel("C:/Users/POOJA KENJALE/Desktop/Financial Sample.xlsx", sheet_name = "Sheet1")
print(df)




# ---------------------------------------------------------------------------------------------------- PRINTING SERIES------------------------------------------------------------------------ 

"""
 A Pandas Series is like a column in a table.
 A Series is a one-dimensional labeled array capable of holding any data type.
 It can be thought of as a single column of data. It has a single index and values associated with that index.

"""

import pandas as pd

data = [12, 23, 56, 45]
my_series = pd.Series(data)
print(my_series)


# If nothing is specified, the values are labeled with their index number. First value has 0, second value has 1, etc.



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




"""

CREATE LABELS: -

We can also name own labels.

"""

import pandas as pd

data = [12, 21, 32]
my_series = pd.Series(data, index = ["x","y","z"])
print(my_series)

# We can access items by created labels i.e.: - refer to above example 

print(my_series["x"])




"""
KEY/VALUE Objects as a Series: - 


you can also use a Key/Value object, like a dictionary, when creating a series.

"""

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}      # python dictionary

my_series = pd.Series(calories)
print(my_series)


# NOTE: - The key of the dictionary becomes labels.




"""
To select more than 1 items in dictionary, use the index argument and specify only items you want to include in the series.

"""

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}      # python dictionary

my_series = pd.Series(calories, index = ["day1", "day2"])
print(my_series)











# ------------------------------------------------------------------------------------------------- PRINTING DATAFRAME------------------------------------------------------------------------


"""
A DataFrame is a two-dimensional labeled data structure with columns that can be of different types.
It can be thought of as a table with rows and columns. Each column in a DataFrame is a Series.

"""

import pandas as pd

data = {
    "cars" : ["Tata", "Mahindra", "Maruti"],            # python dictionary
    "Model" : [2020, 2021, 2018]
}

my_dataframe = pd.DataFrame(data)
print(my_dataframe)






"""

 4.1 Locate Row (loc): - 


DataFrame is like table with rows and columns
Pandas uses 'loc' attribute to return one or more specified rows.


"""

import pandas as pd

data = {
    "cars" : ["Tata", "Mahindra", "Maruti"],            # python dictionary
    "Model" : [2020, 2021, 2018]
}

my_dataframe = pd.DataFrame(data)
print(my_dataframe.loc[0])


# Note: This example returns a Pandas Series.







# If you want to return more than 1 row then: - 

import pandas as pd

data = {
    "cars" : ["Tata", "Mahindra", "Maruti"],            # python dictionary
    "Model" : [2020, 2021, 2018]
}

my_dataframe = pd.DataFrame(data)
print(my_dataframe.loc[[0, 1]])

# Note: When using [], the result is a Pandas DataFrame.







"""

 4.2 Named Index: - 


With index argument, you can name your own indexes.

"""

import pandas as pd

data = {
    "calories" : [420, 120, 100],
    "duration" : [50, 40, 25]
}

my_dataframe = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(my_dataframe)







"""

 4.3 Locate Named Index: - 

# refer the above example
# Use the named index in the loc attribute to return the specified row(s).


"""

print(my_dataframe.loc["day1"])





# ------------------------------------------------------------------------ 5. Loading CSV file into DataFrame ------------------------------------------------------------------------


# If we print DataFrame without to_string() then, it will return first 5 rows and the last 5 rows: -

import pandas as pd

my_dataframe = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/industry.csv")
print(my_dataframe)


# Note: - Use to_string() to print the entire DataFrame

print(my_dataframe.to_string())





# ------------------------------------------------------------------------------------------------- 5.1 max_rows ------------------------------------------------------------------------



"""
The no. of rows returned is defined in pandas option settings.
You can check it by "pd.options.display.max_rows": -

"""

print(pd.options.display.max_rows)


# You can also set the no. of rows to be returned by :- 

pd.options.display.max_rows = 999
print(pd.options.display.max_rows)









# ----------------------------------------------------------------------------------- 6. READING JSON FILE ------------------------------------------------------------------------------



# Big data sets are often stored, or extracted as JSON.

import pandas as pd

my_dataframe = pd.read_json("C:/Users/POOJA KENJALE/Desktop/sample.json")
print(my_dataframe.to_string())







### 6.1 Dictionary as JSON




# 1) The primary difference between JSON and Python dictionary is that JSON is a text-based data format, while a Python dictionary is a data structure.
# 2) The keys in JSON can only Strings. Whereas Keys in Python dictionary can hashable object.

# If JSON code is not in a file, but in a python dictionary then, you can directly load into DataFrame.

import pandas as pd

data = [{
    "fruit" : "Apple",
    "size" : "Large",
    "color" : "Red"
}]

my_dataframe = pd.DataFrame(data)
print(my_dataframe)





# --------------------------------------------------------------------------------- 7. PANDAS ANALYZING DATA -----------------------------------------------------------------------------------

# 7.1 VIEWING THE DATA: - 


# 7.1.1 VIEWING THE DATA FROM TOP: - 


# One of the most used method to get a quick overview of the data is head() method
# The head() returns the headers and a specified number of rows, starting from top 

# Note: - If the number is not specified then, it will print top 5 rows by default.

import pandas as pd

data = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/industry.csv")
print(data.head(10))




### 7.1.2 VIEWING THE DATA FROM BOTTOM: - 



# To view the data(First 5 rows) from the bottom of the DataFrame, tail() is used.
 # tail() returns the header and specified number of rows.

import pandas as pd

data = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/industry.csv")
print(data.tail(10))






### 7.1.3 INFO ABOUT THE DATA: - 



# info() method gives you the information about the data set. [Refer above example]
# As you can see in the o/p that, info() also tells you about Non-Null values or empty values. You should consider removing rows with empty values, and that is called as "Data Cleaning"

print(data.info()) 






# ----------------------------------------------------------------------------------------- 8. DATA CLEANING ------------------------------------------------------------------------





"""
Data Cleaning is the process of removing bad data from the given data set.

Bad Data can be: - 
    1) Empty Cells/Null values
    2) Data in wrong format
    3) Wrong Data
    4) Duplicate data

"""





## 8.1 Cleaning Empty Cells: - 


# empty cells can potentially give you a wrong results when you analyze the data.
# So 1 way is to remove the whole rows which contains the empty value. This is usually ok since data sets can be very big, & removing it will not have big impact on the results.

import pandas as pd

my_dataframe = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/dataset_with_bad_data.csv")
new_dataframe = my_dataframe.dropna()

print(new_dataframe)



# By default, dropna() returns new dataframe. In order to replace in the same dataframe use: - inplace = True

import pandas as pd

my_dataframe = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/dataset_with_bad_data.csv")

my_dataframe.dropna(inplace = True)
print(my_dataframe.to_string())


# Now, inplace = True will not create a new dataframe, but it will remove the rows containing NULL values from the original dataframe.







### 8.1.1 Replace empty values with another value




# one more way to remove the empty values is by replacing it with another value. So that you will not have to delete the row just because it has empty cella.
# It can be done by fillna()


import pandas as pd

my_dataframe = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/dataset_with_bad_data.csv")
my_dataframe.fillna(130, inplace = True)
print(my_dataframe.to_string())







### 8.1.2 Replace empty values with another value only for specified columns: - 



# here we will replace empty values with specified value but only for specified column.


import pandas as pd

my_dataframe = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/dataset_with_bad_data.csv")
my_dataframe['Calories'].fillna(130, inplace = True)    # This will replace empty values from only calories column.
print(my_dataframe)






### 8.1.3 Replace empty values with MEAN/MEDIAN/MODE: - 


#               Mean = the average value (the sum of all values divided by number of values).
#               Median = the value in the middle, after you have sorted all values ascending.
#               Mode = the value that appears most frequently.





# Here first we are calculating MEAN and then replacing empty values with MEAN: - 

import pandas as pd

my_dataframe = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/dataset_with_bad_data.csv")
x = my_dataframe['Calories'].mean()
my_dataframe.fillna(x, inplace = True)
print(my_dataframe)






# Here first we are calculating MEDIAN and then replacing empty values with MEDIAN: - 

import pandas as pd

my_dataframe = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/dataset_with_bad_data.csv")
x = my_dataframe['Calories'].median()
my_dataframe.fillna(x, inplace = True)
print(my_dataframe)







# Here first we are calculating MODE and then replacing empty values with MODE: - 

import pandas as pd

my_dataframe = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/dataset_with_bad_data.csv")
x = my_dataframe['Calories'].mode()[0]
my_dataframe.fillna(x, inplace = True)
print(my_dataframe)







# ------------------------------------------------------------------------ 8.2 Cleaning Wrong Format Data ------------------------------------------------------------------------




"""

 Sometimes it may happen that data set contains cells with wrong data format. In resulting, difficult or even impossible to analyze data.
 There are 2 options: - 
   1) Delete the entire row containing wrong data format
   2) Convert all cells in the column into same format.


"""

# ---------------------------------------------------------------------------------- Delete the entire row containing wrong data format -----------------------------------------------------------------
import pandas as pd


data = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/dataset_with_bad_data.csv")
data.dropna(inplace = True)                                
print(data.to_string())


# OR IF you want to delete Rows with Missing Values in a Specific Column (Date in this case): - 

df.dropna(subset=['Date'], inplace = True)








# ---------------------------------------------------------------------------------- Convert all cells in the column into same format -----------------------------------------------------------------


import pandas as pd


data = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/dataset_with_bad_data.csv")
data['Date'] = pd.to_datetime(data['Date'])                               
print(data.to_string())









# ------------------------------------------------------------------------ 8.3 Cleaning Wrong Data ------------------------------------------------------------------------






"""
"Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".

Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.
 It can be solved by: - 
    1) Replacing the value 
    2) Deleting the entire row

"""


import pandas as pd

data = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/dataset_with_bad_data.csv")
print(data.to_string())


# ---------------------------------------------------------------------------------- Replacing the value -----------------------------------------------------------------


import pandas as pd


data = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/dataset_with_bad_data.csv")
for x in data.index:
    data.loc[7, 'Duration'] = 45                # replacing the value at 7th row with value 45

print(data.to_string())


# The above code is for small dataset, but what if we have big dataset


import pandas as pd


data = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/dataset_with_bad_data.csv")
for x in data.index:
    if data.loc[x, 'Duration'] > 120:
        data.loc[x, 'Duration'] = 45

print(data.to_string())









# ---------------------------------------------------------------------------------- Deleting the entire row -----------------------------------------------------------------


import pandas as pd 


data = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/dataset_with_bad_data.csv")
for x in data.index:
    if data.loc[x, 'Duration'] > 120:
        data.drop(x, inplace = True)

print(data.to_string())







# ------------------------------------------------------------------------ 8.4 Removing Duplicates ------------------------------------------------------------------------







# We can discover duplicate values by: - 

import pandas as pd

data = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/dataset_with_bad_data.csv")
print(data.duplicated())




# And we can delete duplicates by: - 


import pandas as pd

data = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/dataset_with_bad_data.csv")
data.drop_duplicates(inplace = True)











# ------------------------------------------------------------------------ 9. PANDAS CORRELATION ------------------------------------------------------------------------






# corr() method is used to calculate the relationship between each column in your data set.
# Note: - corr() method ignores "non numeric" columns.

import pandas as pd

data = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/data.csv")
print(data.corr())



"""
How to read Results: - 

    - The result of the corr() is a tale with a numbers that represents how well the relationship between 2 columns.
    - The number varies between 1 and -1.
    - 1 means there is 1 to 1 relationship between (a perfect correlation).
    - 0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.
    - (-0.9) is as good as 0.9, but if you increase one value, other might go down.
    - 0.2 is NOT a good relationship, meaning that if one value goes up does not meant other will. 

Now, what is good relationship, It's safe to say 0.6 or (-0.6) is a good relationship.



"""












# ------------------------------------------------------------------------ 10. PANDAS PLOTTING ------------------------------------------------------------------------





"""

pandas uses plot() method to create diagrams.
We can use "Pyplot", a submodule of the "Matplotlib" library to visualize the diagram on screen.
NOTE: - plot() method requires numeric dataset.


"""


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/dataset_with_bad_data.csv")
data.plot()
plt.show()








### 10.1 Scatter Plot: - 


"""
Scatter plot requires x-axis and y-axis.
And it can be done by specifying kind = "scatter"


""" 


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/dataset_with_bad_data.csv")
data.plot(kind = "scatter", x = "Duration", y = "Calories")

plt.show()











### 10.2 Histogram Plot: - 




"""
A histogram need only 1 column.
A histogram can be created by kind = "hist".


"""



import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/POOJA KENJALE/Desktop/dataset_with_bad_data.csv")
data["Calories"].plot(kind = "hist")

plt.show()



















