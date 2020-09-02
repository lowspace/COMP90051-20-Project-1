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
