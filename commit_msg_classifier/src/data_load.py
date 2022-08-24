import os
import re
import string
import math
# DATA_DIR = 'enron'
target_names = ["adjustedszz_bugfix",
    "issueonly_bugfix",
    "testchange_javacode",
    "documentation_technicaldept_add",
    "refactoring_codebased",
    "documentation_technicaldept_remove",
    "refactoring_keyword",
    "documentation_javainline",
    "documentation_javadoc",
    "issueonly_featureadd",
    "validated_bugfix"]

def get_data(msg_nl, class_label_csv):
    data = []
    target = []
    
    with open(msg_nl, 'r') as f: 
        with open(class_label_csv, 'r') as fc:
            for comment, class_line in zip(f.readlines(), fc.readlines()):
                comment = comment.strip()
                one_hot_per_each_class = class_line.strip().replace(" ", '').split(',')[1:]
                count = 0
                one_hot_index = 0
                
                for index, num in enumerate(one_hot_per_each_class):
                    if int(num):
                        one_hot_index = index
                        count += 1
                    if count > 1:
                        break
                if count == 1:
                    data.append(comment)
                    target.append(one_hot_index)
        f.close()
        fc.close()
    return data, target
    # data = ["this is normal commit", "to change version"...]
    # target = [[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], [1,0,0,0,0].....]

def main():
    X, y = get_data("input/msg.nl", "input/input.csv")
    print("len(x)", len(X))
    print("len(Y)", len(y))
    print("y: ", y[:300])

if __name__ == '__main__':
    main()