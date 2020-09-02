train = open(r"C:\Users\19501\OneDrive\Desktop\data\train.txt", "r")
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
#dict{被关注账号：被关注次数（20000博主中）}
follow_freq = {}
for list in follow_dict.values():
    for id in list:
        if id in follow_freq.keys():
            follow_freq[id] += 1
        else:
            follow_freq[id] = 1
#dict{被关注账号：被博主关注概率}
follow_prob = {}
for id in follow_freq.keys():
    follow_prob[id] = follow_freq[id]/len(follow_freq)

#账号被关注概率的有序list
sorted_prob = sorted(follow_prob.items(),key = lambda x:x[1],reverse = True)

#所有被关注账号
nodeB_list = []
for key in follow_freq.keys():
    nodeB_list.append(key)

#dict{博主：该博主关注账号数量}
follow_count = {}
for id in follow_dict.keys():
    follow_count[id] = len(follow_dict[id])


train_data = []
label = []

for A, L in follow_dict.items():
    for B in L:
        train_data.append([A,B])
        label.append(1)