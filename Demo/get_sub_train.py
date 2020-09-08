#!/usr/bin/env python
# coding: utf-8

# In[3]:


train = open("train.txt", "r")
data = train.readlines()
#所有原始数据
follow_list = []
#所有博主id
nodeA_list = []
for line in data:
    list = line.strip("\n").split("\t")
    follow_list.append(list)
    nodeA_list.append(list[0])
#dict{博主，该博主关注列表}
follow_dict = {}
for follow in follow_list:
    follow_dict[follow[0]] = follow[1:]

train_data = []
label = []

for A, L in follow_dict.items():
    for B in L:
        train_data.append([A,B])
        label.append(1)


# In[5]:


import random
random.seed(0)
sub_train = random.sample(train_data, 4000) 
print(sub_train)


# In[29]:


f = open("sub_train.txt", "w")


# In[30]:


i = 1
f.write("ID" +  "\t" + "Source" + "\t" + "Sink" + "\n")
for pair in sub_train:
    f.write( str(i) + "\t" + pair[0] + "\t" + pair[1] + "\n")
    i+=1


# In[31]:


f.close()

