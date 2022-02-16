#!/usr/bin/env python
# coding: utf-8

# # Keywords

# In[ ]:





# In[4]:


help()


# In[ ]:





# In[5]:


#,+,-,*,/,%,//


# In[6]:


print(4+5)


# In[7]:


a=1
b=6
c=a+b
print(c)


# In[8]:


a=9
b=8
print(a+b)


# In[9]:


print(21/5)


# In[10]:


print(21//5)


# In[11]:


print(2*4)


# In[12]:


print(2**4)


# # comparison operator

# In[13]:


#comparison ---------return true or false
# ==, !=, >=, <=, 


# In[16]:


a=5
b=5
c=10
print(c==a+b)
print(a>=c)
print(c==a+b)


# # logical operator

# In[17]:


#AND, OR, NOT


# In[21]:


a=10
b=20
c=30
d=40
print(a+b ==c and c>d)
print(a+b ==c or c>d)
print(not(a+b ==c and c>d))
print(not(a+b ==c or c>d))


# # mutable and immutable

# In[22]:


# a mutable objectv is one whose value may change in place
# whereas in an immutable variable change of value will not happen in place.....


# # identifying operator

# In[24]:


a=10
b=10
print(a==b)
print(a is b)
print( a is not b)


# In[25]:


c=63
d=36
print(c is not b)


# # membership operator

# In[26]:


# in, not, in


# In[31]:


a="python"
print('p' in a)
print('z' in a)
print('p' not in a)
print('z' not in a)
print("z" not in a)


# # DATATYPE
# 
#  # 1. NUMBER
#   # (INT, FLOAT, COMPLEX)

# a=5
# print(a)
# print(type(a))
# b=2.3
# print(type(b))
# c=2+3j
# print(type(c))
# d=a+c
# print(d)
# print(type(d))
# e=1+2i
# print(type(e))

# # * DENOTED BY ''' ''', " ", ' '
# # * CONCATENATION
# # * INDEXING
# # * SLICING
# # * METHODS

# # \n is line break character and 
# # \t is used for giving a tab space 
# a='hey!\n I am \n python \t learner'
# print(a)

# In[44]:


# concatenation
a="hello"
b="student"
print(a+b)
print(a + b)
print(a+' '+b)


# # indexing

# # indexing starts a 0, so the hello:
# 

# In[47]:


# character : h e l l o
# index     : 0 1 2 3 4
# you can use sq. brackets to grab single character
# reverse indexing h e l l e   -5 -4 -3 -2 -1


# In[52]:


a= "python"
print(a[1])
print(a[5])
print(a[0])
print(a[-6])


# In[ ]:




