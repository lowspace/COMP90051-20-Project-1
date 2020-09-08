"""
Data Preprocessing
"""

import os
import re
import pandas as pd

# read train data
file_dir = '../input/comp90051-2020-sem2-proj1/'
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

import multiprocessing as mp
import time

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

def jaccard1(a:str, b:str, graph:dict) -> float:
    SigmaA = getSigma(a, graph)
    SigmaB = getSigma(b, graph)
    return float(len(SigmaA.intersection(SigmaB)) / len(SigmaA.union(SigmaB)))

def jaccard2(a:str, b:str, graph:dict) -> float:
    score = 0
    SigmaOutA = getSigmaOut(a, graph)
    if SigmaOutA:
        for node in SigmaOutA:
            score += jaccard1(b, node, graph)
        return float(score/len(SigmaOutA))
    else:
        return 0
    
def jaccard3(a:str, b:str, graph:dict) -> float:
    score = 0
    SigmaInB = getSigmaIn(b, graph)
    if SigmaInB:
        for node in SigmaInB:
            score += jaccard1(a, node, graph)
        return float(score/len(SigmaInB))
    else:
        return 0

# Jaccard Type 3

import multiprocessing as mp
import time
import copy as cp

train_dic = {}
for item in train_set:
    train_dic[item[0]] = item[1:]
    
if __name__ == '__main__':
    
    def getPro(record:list) -> list:
        node = [record[0], jaccard3(record[1], record[-1], train_dic)]
        print(node)
        return [record[0], jaccard3(record[1], record[-1], train_dic)]
         
    # construct the # of pools corresponding to the cpu_count in ur PC
    pool = mp.Pool(mp.cpu_count())
    
    startTime = time.time()
    
    Jaccard3 = pool.map(getPro, test_set[1850:2000])
    pool.close()
    pool.join()
    
    endTime = time.time()
    print("Total time:" + (endTime - startTime).__str__())

    title = ["Id", "Predicted"]
    test_pd = pd.DataFrame(columns = title, data = Jaccard3)
    test_pd.to_csv('/Jaccard3Score_1850_2000.csv',encoding='utf-8')