#!/usr/bin/env python
# coding: utf-8

# <h3> Question 1 :nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following</h3>
# <ol>
#     <li>What was the average temperature in first week of Jan</li>
#     <li>What was the maximum temperature in first 10 days of Jan</li>
#     </ol>
#     

# In[64]:


nyc_weather = []

with open("C:/Users/prakhar/Desktop/nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            nyc_weather.append(temperature)
        except:
            print("Invalid temperature.Ignore the row")


# In[65]:


nyc_weather


# In[66]:


length = len(nyc_weather)


# In[67]:


sum = 0
for itr in range(0,len(nyc_weather)-3):
    sum = sum + nyc_weather[itr]

    
print(sum/(itr+1))


# In[68]:


max(nyc_weather)


# <h3> Question 2 :nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following</h3>
# <ol>
#     <li>What was the temperature on Jan 9</li>
#     <li>What was the temperature on Jan 4</li>
#     </ol>

# In[69]:


nyc_weather = {} #initializing a dictionary

with open("C:/Users/prakhar/Desktop/nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        try:
            date = tokens[0]
            temperature = int(tokens[1])
            nyc_weather[date] = temperature
        except:
            print("Invalid temperature.Ignore the row")


# In[70]:


nyc_weather


# In[71]:


nyc_weather['Jan 9']


# In[72]:


nyc_weather['Jan 4']


# <h3>Question no3: poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.</h3>
# <br>
# 'diverged': 2,
#  'in': 3,
#  'I': 8</br>

# In[74]:


# Open the file in read mode
text = open("C:/Users/prakhar/Desktop/poem.txt", "r")

# Create an empty dictionary
d = {}

# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()

    # Split the line into words
    words = line.split(" ")

    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

# Print the contents of dictionary
for key in list(d.keys()):
    print(key, ":", d[key])


# In[ ]:





# In[ ]:





# In[ ]:




