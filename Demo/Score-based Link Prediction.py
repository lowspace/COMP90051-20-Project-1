"""
Data Preprocessing
"""

import os
import re
import pandas as pd

# read train data
file_dir = '/Users/dnhb/PycharmProjects/SML_Ass1'
file_name = "train.txt"

def parse(data:list)->list: 
    # Python Notation: https://www.python.org/dev/peps/pep-3107/
    """
    Prase each line of the data
    Return a nested list, such as [[id1, id2, id2,...],...]
    """
    parsed_data = []
    for line in data:
        # remove \n at the end of each line
        line = re.sub(r"(?<=\d)\n", "", line)
        # split IDs by \t
        pattern = re.compile("(?<=\d)\t(?=\d)")
        line = re.split(pattern, line)
        parsed_data.append(line)
    return parsed_data

with open(os.path.join(file_dir, file_name)) as f:
    train_set = f.readlines()
    train_set = parse(train_set)
    
# read test data
test_name = "test-public.txt"
with open(os.path.join(file_dir, test_name)) as f:
    test_set = f.readlines()
    test_set = parse(test_set)
    test_set.pop(0)

# turn ID into int
for i in range(0, len(test_set)):
    test_set[i][0] = int(test_set[i][0])

# Similarity

train_dic = {}
for item in train_set:
    train_dic[item[0]] = item[1:]

def getSigma(node:str, graph:dict) -> set:
    SigmaOut = getSigmaOut(node, graph)
    SigmaIn = getSigmaIn(node, graph)
    Sigma = SigmaIn.union(SigmaOut)
    return Sigma

def getSigmaOut(node:str, graph:dict) -> set:
    SigmaOut = set()
    try:
        for item in graph[node]:
            SigmaOut.add(item)
        return SigmaOut
    except:
        return SigmaOut

def getSigmaIn(node:str, graph:dict) -> set:
    SigmaIn = set()
    for key, value in graph.items():
        if node in value:
            SigmaIn.add(key)
    return SigmaIn

# Jaccard Type 1

def jaccard1(a:str, b:str, graph:dict) -> float:
    SigmaA = getSigma(a, graph)
    SigmaB = getSigma(b, graph)
    return float(len(SigmaA.intersection(SigmaB)) / len(SigmaA.union(SigmaB)))

train_dic = {}
for item in train_set:
    train_dic[item[0]] = item[1:]

Jaccard1 = []
for ID, user, sink in test_set:
    Jaccard1.append([ID, jaccard1(user, sink, train_dic)])

# sort the results
Jaccard1_result = sorted(Jaccard1, key=lambda x: x[-1], reverse=True)
for item in Jaccard1_result:
    index = Jaccard1_result.index(item)
    if index < len(Jaccard1_result)/2:
        Jaccard1_result[index][-1] = 1
    else:
        Jaccard1_result[index][-1] = 0
Jaccard1_result = sorted(Jaccard1_result, key=lambda x: x[0], reverse=False)

# output
title = ["Id", "Predicted"]
test_pd = pd.DataFrame(columns = title, data = Jaccard1_result)
test_pd.to_csv('/Users/dnhb/PycharmProjects/SML_Ass1/Jaccard1.csv', encoding='utf-8')

## Jaccard type 2

def jaccard2(a:str, b:str, graph:dict) -> float:
    score = 0
    SigmaOutA = getSigmaOut(a, graph)
    if SigmaOutA:
        for node in SigmaOutA:
            score += jaccard1(b, node, graph)
        return float(score/len(SigmaOutA))
    else:
        return 0

train_dic = {}
for item in train_set:
    train_dic[item[0]] = item[1:]
    
Jaccard2 = []
for ID, user, sink in test_set:
    Jaccard2.append([ID, jaccard2(user, sink, train_dic)])
    
Jaccard2_result = sorted(Jaccard2, key=lambda x: x[-1], reverse=True)
for item in Jaccard2_result:
    index = Jaccard2_result.index(item)
    if index < len(Jaccard2_result)/2:
        Jaccard2_result[index][-1] = 1
    else:
        Jaccard2_result[index][-1] = 0
Jaccard2_result = sorted(Jaccard2_result, key=lambda x: x[0], reverse=False)

title = ["Id", "Predicted"]
test_pd = pd.DataFrame(columns = title, data = Jaccard2_result)
test_pd.to_csv('/Users/dnhb/PycharmProjects/SML_Ass1/Jaccard2.csv',encoding='utf-8')

## Jaccord type 3
def jaccard3(a:str, b:str, graph:dict) -> float:
    score = 0
    SigmaInB = getSigmaIn(b, graph)
    if SigmaInB:
        for node in SigmaInB:
            score += jaccard1(a, node, graph)
        return float(score/len(SigmaInB))
    else:
        return 0

train_dic = {}
for item in train_set:
    train_dic[item[0]] = item[1:]
    
Jaccard3 = []
for ID, user, sink in test_set:
    Jaccard3.append([ID, jaccard3(user, sink, train_dic)])
    
Jaccard3_result = sorted(Jaccard3, key=lambda x: x[-1], reverse=True)
for item in Jaccard3_result:
    index = Jaccard3_result.index(item)
    if index < len(Jaccard3_result)/2:
        Jaccard3_result[index][-1] = 1
    else:
        Jaccard3_result[index][-1] = 0
Jaccard3_result = sorted(Jaccard3_result, key=lambda x: x[0], reverse=False)

title = ["Id", "Predicted"]
test_pd = pd.DataFrame(columns = title, data = Jaccard3_result)
test_pd.to_csv('/Users/dnhb/PycharmProjects/SML_Ass1/Jaccard3.csv',encoding='utf-8')
