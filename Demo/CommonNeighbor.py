# train = open(r"C:\Users\19501\OneDrive\Desktop\SML\ASS1\data\train.txt", "r")
# test = open(r"C:\Users\19501\OneDrive\Desktop\SML\ASS1\data\test-public.txt", "r")
# sub_train =
"""
Data Preprocessing
"""

import os
import re
import time
from typing import List, Any, Union

import pandas as pd
import multiprocessing as mp
import copy as cp
# read train data
file_dir = '/Users/19501/OneDrive/Desktop/SML/ASS1/data'
file_name = "train.txt"


def parse(data: list) -> list:
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
# test_name = "test-public.txt"
# with open(os.path.join(file_dir, test_name)) as f:
#     test_set = f.readlines()
#     test_set = parse(test_set)
#     test_set.pop(0)
#
# # turn ID into int
# for i in range(0, len(test_set)):
#     test_set[i][0] = int(test_set[i][0])

sub_train_name = "sub_train.txt"
with open(os.path.join(file_dir, sub_train_name)) as f2:
    sub_train_set = f2.readlines()
    sub_train_set = parse(sub_train_set)
    sub_train_set.pop(0)

# turn ID into int
for i in range(0, len(sub_train_name)):
    sub_train_set[i][0] = int(sub_train_set[i][0])

for i in range(0, len(sub_train_set)):
    sub_train_set[i][0] = int(sub_train_set[i][0])
# Similarity

train_dic = {}
for item in train_set:
    train_dic[item[0]] = item[1:]


def getSigma(node: str, graph: dict) -> set:
    SigmaOut = getSigmaOut(node, graph)
    SigmaIn = getSigmaIn(node, graph)
    Sigma = SigmaIn.union(SigmaOut)
    return Sigma


def getSigmaOut(node: str, graph: dict) -> set:
    SigmaOut = set()
    try:
        for item in graph[node]:
            SigmaOut.add(item)
        return SigmaOut
    except:
        return SigmaOut


def getSigmaIn(node: str, graph: dict) -> set:
    SigmaIn = set()
    for key, value in graph.items():
        if node in value:
            SigmaIn.add(key)
    return SigmaIn


# Common Neighbors Type 1
def common_neighbors1(a: str, b: str, graph: dict) -> float:
    SigmaA = getSigma(a, graph)
    SigmaB = getSigma(b, graph)
    return len(SigmaA.intersection(SigmaB))

# Common_neighbors1 = []
# for ID, user, sink in test_set:
#     Common_neighbors1.append([ID, common_neighbors1(user, sink, train_dic)])

# sort the results

# Common_neighbors1_result = sorted(Common_neighbors1, key=lambda  x:x[-1], reverse=True)
# for item in Common_neighbors1_result:
#     index = Common_neighbors1_result.index(item)
#     if index < len(Common_neighbors1_result) / 2:
#         Common_neighbors1_result[index][-1] = 1
#     else:
#         Common_neighbors1_result[index][-1] = 0
# Common_neighbors1_result = sorted(Common_neighbors1_result, key=lambda x: x[0], reverse=False)

# output


# title = ["Id", "Predicted"]
# test_pd = pd.DataFrame(columns=title, data=Common_neighbors1_result)
# test_pd.to_csv('/Users/19501/OneDrive/Desktop/Common_neighbors1.csv', encoding='utf-8')
# print("type 1 finished")

#Common neighbors type 2


# def common_neighbors2(a: str, b: str, graph: dict) -> float:
#     score = 0
#     SigmaOutA = getSigmaOut(a, graph)
#     if SigmaOutA:
#         for node in SigmaOutA:
#             score += common_neighbors1(b, node, graph)
#         return float(score / len(SigmaOutA))
#     else:
#         return 0

def getPro(record: list) -> list:
    node= [record[0], common_neighbors1(record[1], record[-1], train_dic)]
    print(node)
    return node

if __name__ == '__main__':

    # construct the # of pools corresponding to the cpu_count in ur PC
    pool = mp.Pool(mp.cpu_count())
    startTime = time.time()
    #Common_neighbors1test = pool.map(getPro, test_set)
    Common_neighbors1sub_train = pool.map(getPro, sub_train_set)
    pool.close()
    pool.join()

    endTime = time.time()
    print("Total time:" + (endTime - startTime).__str__())

    title = ["Id", "Predicted"]
    #test_pd = pd.DataFrame(columns=title, data=Common_neighbors1test)
    #test_pd.to_csv('/Users/19501/OneDrive/Desktop/SML/ASS1/data/Common_neighbors1TestScore.csv', encoding='utf-8')
    test_pd = pd.DataFrame(columns=title, data=Common_neighbors1sub_train)
    test_pd.to_csv('/Users/19501/OneDrive/Desktop/SML/ASS1/data/Common_neighbors1SubtrainScore.csv', encoding='utf-8')
# print("type 2 finished")


# Common neighbors Type3


# def common_neighbors3(a: str, b: str, graph: dict) -> float:
#     score = 0
#     SigmaInB = getSigmaIn(b, graph)
#     if SigmaInB:
#         for node in SigmaInB:
#             score += common_neighbors1(b, node, graph)
#         return float(score / len(SigmaInB))
#     else:
#         return 0

# if __name__ == '__main__':
#     def getPro(record:list) -> list:
#         node = [record[0],common_neighbors3(record[1],record[-1],train_dic)]
#         print(node)
#         return [record[0],common_neighbors3(record[1],record[-1],train_dic)]
#
#     pool = mp.Pool(mp.cpu_count())
#     startTime = time.time()
#     Common_neighbors3 = pool.map(getPro, test_set[:2])
#     pool.close()
#     pool.join()
#     endTime = time.time()
#
#     print("Total_time:" + (endTime - startTime).__str__())
#
#     Common_neighbors3_result = sorted(Common_neighbors3, key=lambda  x:x[-1], reverse=True)
#     Common_neighbors3_result = cp.deepcopy(Common_neighbors3_result)
#     for item in Common_neighbors3_result:
#         index = Common_neighbors3_result.index(item)
#         if index < len(Common_neighbors3_result) / 2:
#             Common_neighbors3_result[index][-1] = 1
#         else:
#             Common_neighbors3_result[index][-1] = 0
#     Common_neighbors3_result = sorted(Common_neighbors3_result, key=lambda x: x[0], reverse=False)
#     title = ["Id", "Predicted"]
#     test_pd = pd.DataFrame(columns=title, data=Common_neighbors3_result)
#     test_pd.to_csv('/Users/19501/OneDrive/Desktop/Common_neighbors3.csv', encoding='utf-8')
#     test_pd = pd.DataFrame(columns = title, data = Common_neighbors3)
#     test_pd.to_csv('/Users/19501/OneDrive/Desktop/Common_neighbors3Score.csv', encoding='utf-8')
# Common_neighbors3 = []
# for ID, user, sink in test_set:
#     Common_neighbors3.append([ID, common_neighbors3(user, sink, train_dic)])
