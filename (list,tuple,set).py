#!/usr/bin/env python
# coding: utf-8

# In[1]:


s="Data Science"
len(s)


# In[2]:


s.find("e")
# finds first occurance


# In[3]:


s.count("e")


# In[4]:


s.capitalize()
# first letter capital


# In[5]:


s.upper().lower()


# In[6]:


#str + number
s = s +' 1'
# temporary stored at new location
s


# In[7]:


s*3
#division not supported


# # LIST

# In[8]:


l1=["python","jupyter",[1,2,3],True,24,76]


# In[9]:


l1+s


# In[10]:


#list as a function
list(s)
# breaks elements and store


# In[11]:


l1+list(s)


# In[12]:


#list as a function
list(s)
# breaks elements and store


# In[13]:


# accessing list in list
l1[2][2]


# In[14]:


# part of bool inside list
l1[3][1]


# In[15]:


str(l1[3])


# In[16]:


q= str(l1[3])[0:2]
q


# In[17]:


# list + list
l=[1,2,3,4]
l+l1


# In[18]:


l.append(2) # append only at last
l


# In[19]:


l1.append(s)
l1


# In[21]:


# extend-> takes iterable data,  unwrap and store
l1.extend(l)
l1


# In[22]:


l.extend(s)
l


# In[24]:


# insert->  used to store at a given position
l.insert(2,"Vansh")
l


# In[25]:


l2=["DSA", "CP","WEB DEV","DATA SCIENCE"]
l2.insert(-1,"JAVA")


# In[27]:


l2
# -1 pe hi store kiya,next element aage forward ho gya


# In[28]:


# Removing from list
l2.pop(0)


# In[29]:


l2


# In[32]:


l3=["DSA", "CP","WEB DEV","DATA SCIENCE","Video Editing","DSA"]


# In[34]:


l3.remove("DSA")
l3
# removes first occurance


# In[35]:


# from list in list
l4=[[1,2,3,4],[2,2,3,3]]
l4[1].remove(3)


# In[36]:


l4


# In[39]:


# reverse
l3[::-1]
# temporary


# In[40]:


l3


# In[45]:


l3.reverse()  # permanent


# In[46]:


l3


# In[50]:


l5=[2,45,67,0,23]
l5.sort()
# sort in ascending order
l5


# In[51]:


l5.append("Vansh")
l5


# In[54]:


l5.sort()
# between similar data types


# In[55]:


# descending order
l5.pop()
l5


# In[57]:


l5.sort(reverse=True)
l5


# In[58]:


s


# In[61]:


s.replace('D','d') # temporary


# # Tuple

# In[64]:


#list-> mutable
# tuple-> immutable

t=("badminton","basketball","volleyball")

# only index and count function


# In[65]:


t.index("basketball")


# # Set

# In[68]:


s1={}
type(s1)
# type = dict when set is empty


# In[69]:


s2={2,3,3,4,5,5}


# In[71]:


s2
# stores only unique element


# In[87]:


# list inside set
s3={"sports","study",[3,6,9]}
s3
# stores only immutable element, (list is mutable)


# In[88]:


l6=[3,3,4,5,6,6,7,"vansh","Vansh",(1,2,4)]


# In[89]:


# set as a function
set(l6)


# In[90]:


# remove duplicate elements from a list with help of set
l7={3,4,5,5,6,6,7,7,8,(2,3,5,6),True,2+10j}


# In[91]:


set(l7)


# In[92]:


l7=list(set(l7))
l7


# In[98]:


# no slicing, no indexing
s2[0]


# In[100]:


s2.add(6)
s2


# In[ ]:




