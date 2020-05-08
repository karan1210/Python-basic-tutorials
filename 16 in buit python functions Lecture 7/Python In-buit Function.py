#!/usr/bin/env python
# coding: utf-8

# # 16 In-buit Python Functions

# In[47]:


import docx2txt
my_text = docx2txt.process("Basic inbuilt commands.docx")
print(my_text)


# In[62]:


k = abs(-16.23)
print(k)


# In[65]:


# The all() function returns True if all items in an iterable are true, otherwise it returns False.

# If the iterable object is empty, the all() function also returns True.


k = all('0')
print(k)

# In which case all function print "FALSE" 

myset = {0, 1, 0}
x = all(myset) # ALL 
print(x)

#If you replace all 0s by 1s, then list is iterable and in that case you find "TRUE"

#Use of any function.

myset = {0, 1, 0}
x = any(myset)
print(x)


# In[66]:


binary = bin(100)

print(binary)

# Make sure that "0b" is prefix 


# In[76]:


# OR gate

x = bool(11)

print(x)


# In[77]:


k = bytearray(7)
k


# In[78]:


k = bytes(4)
k


# In[79]:


# Try call function
def karan(): 
    return 5
  
# an object is created of karan() 

let = karan 
print(callable(let)) 
  
# a test variable 

def python():
    num_1 = 15 * 15

num = python

print(callable(num))


# In[83]:


k = chr(100)
k


# In[84]:


#It return complex number 

k = complex(2,3)
print(k)

# If you want to find value of complex number then...
# solution of complex

print(abs(k))


# In[40]:


# delattr() Deletes the specified attribute (property or method) from the specified object
# If you made class then form that class you can delete the elements. 


# In[49]:


# Returns a dictionary (Array)
x = dict(name = "Karan", age = 21, country = "India")

print(x)


# In[85]:


# Display the quotient and the remainder of number_1 divided by number_2:

number_1 = 10
number_2 = 2

x = divmod(number_1, number_2)

print(x)


# In[58]:


# make a list 

x = ('A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P')

y = enumerate(x)

print(list(y))


# In[60]:


#Use for evaluation of code
x = 'print(55)'
eval(x)


# In[ ]:





# In[ ]:




