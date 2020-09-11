#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


#所有被关注账号
nodeB_set = set()
for value in follow_dict.values():
    for i in value:
        nodeB_set.add(i)
print(len(nodeB_set))


# In[8]:


nodeB_list = []
for i in nodeB_set:
    nodeB_list.append(i)


# In[55]:


import random
random.seed(0)
sub_train = random.sample(train_data, 4000) 
print(sub_train)


# In[29]:


import random
random.seed(0)
nodeA_sample = []
nodeA_sample = random.sample(nodeA_list, 200) 


# In[30]:


print(nodeA_sample)


# In[31]:


terminal = []
for i in nodeA_sample:
    terminal.append(follow_dict[i])


# In[32]:


nodeB_terminal = set()
for list in terminal:
    for i in list:
        nodeB_terminal.add(i)


# In[33]:


nodeB_sample = []
for i in nodeB_terminal:
    nodeB_sample.append(i)


# In[34]:


print(len(nodeB_sample))


# In[35]:


positive_list = []
for A in nodeA_sample:
    for B in follow_dict[A]:
        positive_list.append([A,B])
print(len(positive_list))


# In[39]:


sample = []
for A in nodeA_sample:
    for B in nodeB_sample:
        sample.append([A,B])


# In[40]:


len(sample)


# In[49]:


sample2 = random.sample(sample,5000)


# In[50]:


neg_list = [i for i in sample2 if i not in positive_list]


# In[52]:


print(neg_list)


# In[57]:


for i in neg_list[:4000]:
    sub_train.append(i)
print(len(sub_train))


# In[58]:


f = open("sub_train.txt", "w")
i = 1
f.write("ID" +  "\t" + "Source" + "\t" + "Sink" + "\n")
for pair in sub_train:
    f.write( str(i) + "\t" + pair[0] + "\t" + pair[1] + "\n")
    i+=1
f.close()

