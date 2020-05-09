#!/usr/bin/env python
# coding: utf-8

# In[1]:


import docx2txt
my_text = docx2txt.process("Basic inbuilt commands.docx")
print(my_text)


# In[3]:


# filter()

# what filter function do ? 

# filter(function, iterable)

# function:   A Function to be run for each item in the iterable
# iterable:   The iterable to be filtered

# for example: you define name = [xvc, ohg, ger, gea, y4eg,] then name is iterable


# In[50]:


x = float("3.5000000")
x


# In[52]:


x = format(0.75, '+')
x

#format The format you want to format the value into.

#Legal values:
#'<' - Left aligns the result (within the available space)
#'>' - Right aligns the result (within the available space)
#'^' - Center aligns the result (within the available space)
#'=' - Places the sign to the left most position
#'+' - Use a plus sign to indicate if the result is positive or negative
#'-' - Use a minus sign for negative values only
#',' - Use a comma as a thousand separator
#'_' - Use a underscore as a thousand separator
#'b' - Binary format
#'o' - Octal format
#'x' - Hex format, lower case
#'X' - Hex format, upper case
#'n' - Number format
#'%' - Percentage format


# In[55]:


help()

#Try it on your computer


# In[57]:


h = hex(10)
h

# 0x is prefix


# In[58]:


input('write your name here:  ')


# In[59]:


x = 8356298.23590259025
x = int(x)
x


# In[61]:


name = ["k", "a", "r", "a", "n"]
x = len('karan_patel')
x


# In[72]:


marks = [6.97, 7.93, 7.93, 8.3, 8.7 , 9.3, 9.30000000001]

x = max(marks)
print('max', x)

M = min(marks)
print('min', M )


# In[73]:


# Convert the number into an octal value:

x = oct(12321)
x

#0o is prefix


# In[74]:


# print

print("Hello", "how are you?", sep =" ______ ")


# In[75]:


x = range(10)
print(x)
for n in x:
  print(n)


# In[76]:


x = sum(marks)
x


# In[ ]:




