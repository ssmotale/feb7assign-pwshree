#!/usr/bin/env python
# coding: utf-8

# In[10]:


"""

Q1. You are writing code for a company. The requirement of the company is that you create a python
function that will check whether the password entered by the user is correct or not. The function should
take the password as input and return the string “Valid Password” if the entered password follows the
below-given password guidelines else it should return “Invalid Password”.

Note: 1. The Password should contain at least two uppercase letters and at least two lowercase letters.
2. The Password should contain at least a number and three special characters.
3. The length of the password should be 10 characters long. done
"""



  
def ispasswordval(password):
    upper_letter = 0
    lower_letter = 0
    number = 0
    special_characters = 0
    
    if len(password) != 10:
        return 'Invalid Password'
    
    for i in range(len(password)):
        if password[i].isupper():
            upper_letter += 1
        elif password[i].islower():
            lower_letter += 1
        elif password[i].isdigit():
            number += 1
        else:
            special_characters += 1
    
    if upper_letter < 2 or lower_letter < 2 or number < 1 or special_characters < 3:
        return 'Invalid Password'
    else:
        return 'Valid Password'
    
str2="SMab1@#$12"    
ispasswordval(str2)   


# In[22]:


"""

Q2. Solve the below-given questions using at least one of the following:
1. Lambda function
2. Filter function
3. Zap function
4. List Comprehension
B Check if the string starts with a particular letter
B Check if the string is numeric
B Sort a list of tuples having fruit names and their quantity. [("mango",99),("orange",80), ("grapes", 1000)-
B Find the squares of numbers from 1 to 10
B Find the cube root of numbers from 1 to 10
B Check if a given number is even
B Filter odd numbers from the given list.
[1,2,3,4,5,6,7,8,9,10-
B Sort a list of integers into positive and negative integers lists.
[1,2,3,4,5,6,-1,-2,-3,-4,-5,0]

"""
# Check if the string starts with a particular letter
str1="veSNM"
l=list(str1)
a=list(filter(lambda l:l[0]=="A",l))
a
if len(a)>0:
    print("yes it is present")
else:
    print("not present")
    
    
    


# In[40]:


#Check if the string is numeric
is_numeric = lambda string: string.isnumeric()
result = is_numeric("123")
if print(result) ==True:
    print("string is numeric")

        
    


# In[41]:


# Sort a list of tuples having fruit names and their quantity. [("mango",99),("orange",80), ("grapes", 1000)

fruits = [("mango",99),("orange",80),("grapes",1000)]
sorted_fruits = sorted(fruits, key=lambda fruit: fruit[1])
print(sorted_fruits) 


# In[42]:


# Find the squares of numbers from 1 to 10

numbers = [1,2,3,4,5,6,7,8,9,10]
squares = list(map(lambda x: x**2, numbers))
print(squares) 



# In[44]:


# Find the cube root of numbers from 1 to 10

numbers = [1,2,3,4,5,6,7,8,9,10]
squares = list(map(lambda x: x**3, numbers))
print(squares) 



# In[48]:


#Check if a given number is evenY
is_even = lambda x: x % 2 == 0
result = is_even(4)
print(result) 


# In[ ]:


#Filter odd numbers from the given list.
numbers = [1,2,3,4,5,6,7,8,9,10]
oddnumbers = list(filter(lambda x: x % 2 != 0, numbers))
print(oddnumbers) 


# In[51]:


#Sort a list of integers into positive and negative integers lists.
numbers = [1,2,3,4,5,6,-1,-2,-3,-4,-5,0]
positive_numbers = sorted(list(filter(lambda x: x > 0, numbers)))
negative_numbers = sorted(list(filter(lambda x: x < 0, numbers)))
print("Positive numbers:", positive_numbers) 
print("Negative numbers:", negative_numbers)  


# In[ ]:




