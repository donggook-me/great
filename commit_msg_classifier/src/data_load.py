import os
import re
import string
import math
from pathlib import Path

def get_data(msg_nl, class_label_csv):
    # list contain tuple -> (msg, label)
    msg_with_label = []
    
    fm = open(msg_nl, 'r')
    fl = open(class_label_csv, 'r') 
    
    for comment, class_line in zip(fm.readlines(), fl.readlines()):
        labels = list(map(int, class_line.split(', ')[2:]))
        
        if sum(labels) == 1:
            msg_with_label.append((comment.strip(), labels.index(1)))
    
    fm.close()
    fl.close()
            
    return msg_with_label
    # data = ["this is normal commit", "to change version"...]
    # target = [8,2,0,2,2,2,2,2,4,2,2,2.....] number means index of target_names

def main():
    root_path = str(Path(__file__).parent.parent.resolve())
    X, y = get_data(root_path + "/input/msg.nl", root_path + "/input/input.csv")
    print("len(x)", len(X))
    print("len(Y)", len(y))

if __name__ == '__main__':
    main()