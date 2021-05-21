#!/usr/bin/env python
# coding: utf-8

# <h3>Where we Use HashMaps/Dictionary over Lists</h3>

# In[10]:


stock_prices = [] #Initializing a blank List 
with open("C:/Users/prakhar/Desktop/Stock_Prices.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day,price])


# In[11]:


stock_prices 


# <p style="font-size:15px">Time complexity to find a stock on a particular day is <b>O(n)</b>, so this makes it slow and inefficient when we have a large dataset and our element is at the last so it would have to traverse the whole list which would not be efficient to find the element</p>

# In[12]:


stock_prices[0] 


# In[13]:


stock_prices = {} #Initializing a blank Dictionary  
with open("C:/Users/prakhar/Desktop/Stock_Prices.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price


# In[14]:


stock_prices


# <p style="font-size:15px">Time complexity to find a stock on a particular day in a dictionary is <b>O(1)</b>,this makess it more efficient and less time consuming , dictionary uses <b>Hash Function</b> to assign the key value to the index of the value, and more over the dictionary uses String index instead of integer index to locate or find the value </p>

# In[15]:


stock_prices['March 6']


# <h3> Now the Question what is hash Table </h3>

# <p> Hash Table is the underlying data structure and Dictionary is just the python implementation of it .Hash Table uses Hash Function to convert the hash key to the index where the value is stored<p><p>Below is a Image to make you understand more how hash Function Works</p>

# In[16]:


from IPython.display import Image
Image(filename='C:/Users/prakhar/Desktop/Python_Data_Structures_and_Algorithms_Implementations/Images/Hash_Function_1.png',width=800, height=400)
#save the images from github to your local machine and then give the absolute path of the image 


# <h3>Python Implementation of One Type of Hash Table</h3>

# <p> This is one type of Python Function where we will be using the ASCII Value of the String Index and Adding and Dividing it by 100 to get a index where our value will be stored <p> 

# In[18]:


ord('a')


# In[19]:


ord('A')


# In[17]:


def get_hash(key):
    hash = 0
    for char in key:
        hash += ord(char)# this is a python in built function which returns the ASCII value of the argument i have give the example above
    return hash % 100


# In[20]:


get_hash('march 6')#Now you would wonder how did come right 


# In[21]:


from IPython.display import Image
Image(filename='C:/Users/prakhar/Desktop/Python_Data_Structures_and_Algorithms_Implementations/Images/Hashing.png',width=800, height=400)
#save the images from github to your local machine and then give the absolute path of the image 


# So as the Sum was 609 therefore 609%100 = 9 , so the value of Key march 6 will be stored at index 9 

# In[38]:


class HashTable:   #Helper Function for HashTable 
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def add(self,key,val):#here we get the value of a at index b ,operator.__getitem__(a, b) 
        hash = self.get_hash(key)
        self.arr[hash] = val
    
    def get(self,key):
        hash = self.get_hash(key)
        return self.arr[hash]
    
        
     
    


# In[39]:


t = HashTable()
t.add('march 6',130)


# In[40]:


t.arr # if you see here we have stored the value 130 at index no. 9 


# In[42]:


t.get('march 6') #this returns the value for that index


# <h3> Now there is much better way to do the above task which is similar to calling a dictionary index and its value</h3>
#     

# In[43]:


class HashTable:  
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, index): #this is a in built function in python which Return the value of a at index b.
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val): # this is a in built function in python which Set the value of a at index b to c.
        h = self.get_hash(key)
        self.arr[h] = val    
        
    def __delitem__(self, key): #this is a in built function in python which Remove the value of a at index b.
        h = self.get_hash(key)
        self.arr[h] = None


# In[44]:


t = HashTable()
t["march 6"] = 310 # see the difference here we need no call or create any add or get function here we can call in the dictionary style of calling
t["march 7"] = 420


# In[45]:


t.arr # The Hash Function is explained above how the values are store here 


# In[46]:


t["dec 30"] = 88


# In[47]:


t["dec 30"]


# In[48]:


del t["march 6"] #deleting the value at index 9 or march 6 


# In[49]:


t.arr


# In[ ]:




