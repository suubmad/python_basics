# -*- coding: utf-8 -*-
"""
Python basics 

Learning by doing python basics

@author: suubmad Berkay SEN
"""
## %%  divide as a part

#%% 
# variables

var = 20
print(var)
var1 = 40
print(var1)

print(var+var1)

var_str = 'Hello, World'
print(var_str)

#%% 

# string

var_word = 'Space'
print(var_word)
var_type = type(var_word) # type() function returns its type
print(var_type)

long_word = "fibonacci sequence"
print(long_word)
word_length = len(long_word)
print("Word's length is: ",word_length)

# %%
# numbers

# integer

integer_example = 100

print(type(integer_example))

# float

float_example = -25.8

print(type(float_example))

# %%

# def function

a = 40
b = 50

def add_fnc(a, b):
    """
    Parameters
    ----------
    a : TYPE
        DESCRIPTION.
    b : TYPE
        DESCRIPTION.
        
        (+ /- /* ) you can use these
    Returns
    -------
    None.
    """
    output = (a+b) 
    return output

func_result = add_fnc(a, b)
print(func_result)

# %%

# lambda function

# I do the above process with lambda
a = 40
b = 50
l_func = lambda a: a+b
print(l_func(a))

# multiplication
l_func2 = lambda x: x*x
print(l_func2(3))


# %%

# list
"""
dir(my_list)       this shows what can we use
 'append'
 'clear'
 'copy'
 'count'
 'extend'
 'index'
 'insert'
 'pop'
 'remove'
 'reverse'
 'sort
 """
my_strList = ['mohello',123,'hello'] # list can string tho
print(my_strlist)
my_list = [1,2,3,4]
my_list.append(55)                   # append means add in list a number its 55
print(my_list)
my_list.insert(1,15)                 # insert add number with indexing
print(my_list)
my_list.remove(15)                   # remove a item
print(my_list.pop())                 # take last added item
my_list.reverse()
print(my_list)

# %%
# tuple

# NOT LIKE LIST
"""
'count'    we can use
'index'
"""

my_tuple = (1,2,3,4,5,6,8,8)

dir(my_tuple)

print(my_tuple.count(8)) # how many have 8?   answer is 2
print(my_tuple.index(3)) # 3 in which index?  answer is 2
print(my_tuple.index(8))

# %%

# dictionary
# dictionary has keys and values
# this example 
# A, B, C = KEYS
# 50, 100, 150 = VALUES

my_dict = { "A" : 50, 'B' : 100, 'C': 150}

print(my_dict['A'])
print(my_dict['B'])
print(my_dict['C'])

#%%
# if / else
"""
Equals:                     a == b
Not Equals:                 a != b
Less than:                  a <  b
Less than or equal to:      a <= b
Greater than:               a >  b
Greater than or equal to:   a >= b
"""

a = 100
b = 50

if a > b:
    print(b,' is greater then ', a)

my_list = [1,2,3,4]
value = 4 

if value in my_list:
    print("yes {} in list".format(value))
else:
    print('no')

# %%
# for each

for each in range(1,11):
    print(each)
    
my_list = [1,2,3,4]

count = 0

for each in my_list:
    count = count + each
    print(count)
