import os
import re
import string
import math

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
    # target = [8,2,0,2,2,2,2,2,4,2,2,2.....] number means index of target_names

def main():
    X, y = get_data("../input/msg.nl", "../input/input.csv")
    print("len(x)", len(X))
    print("len(Y)", len(y))

if __name__ == '__main__':
    main()