import os
import re

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
    test_set = parse(test_name)

# read test data
test_name = "test-public.txt"
with open(os.path.join(file_dir, test_name)) as f:
    test_set = f.readlines()
    test_set = parse(test_set)
    test_set.pop(0)


# three degree connection theory
train_dic = {}
for item in train_set:
    train_dic[item[0]] = item[1:]
    
test_result = []
for ID, user, sink in test_set:
    result = []
    result.append(ID)
    if sink in train_dic[user]:
        result.append(1)
        continue
    else:
        for friend in train_dic[user]:
            if friend in train_dic.keys():
                if sink in train_dic[friend]:
                    if result[-1] == 1:
                        result.append(1)
                        break
                else:
                    for friend2 in train_dic[friend]:
                        if friend2 in train_dic.keys():
                            if sink in train_dic[friend2]:
                                if result[-1] == 1:
                                    pass
                                else:
                                    result.append(1)
                                    break
    test_result.append(result)

# shape test_result into [id, prediction] pattern
test = []
for item in test_result:
    if 1 in item[1:]:
        test.append([item[0], 1])
    else:
        test.append([item[0], 0])

# output the resutls
import pandas as pd

title = ["Id", "Predicted"]
test_pd = pd.DataFrame(columns = title, data = test)
test_pd.to_csv('/Users/dnhb/PycharmProjects/SML_Ass1/3_degree.csv',encoding='utf-8')