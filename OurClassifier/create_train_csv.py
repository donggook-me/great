# Import python driver for mongoDB
from pymongo import MongoClient
from pymongo.cursor import CursorType
from sklearn.metrics import f1_score
from os import listdir, system, chdir, getcwd
from pathlib import Path
import pandas as pd
import re
        
# Find from DB
def find_from_mongo(client, dbs, collection, query, projection: dict):
    # Make a target list of projection
    fields = dict.fromkeys(projection, True)
    return client[dbs][collection].find(query, projection)

def create_csv(result):
    labels = ['adjustedszz_bugfix', 'issueonly_bugfix', 'testchange_javacode',
        'documentation_technicaldept_add', 'refactoring_codebased', 'documentation_technicaldept_remove',
        'refactoring_keyword', 'documentation_javainline', 'documentation_javadoc',
        'issueonly_featureadd', 'validated_bugfix']
    
    with open('final_input.csv', 'w') as f:
        for ln in result:
            target = re.sub("[0-9]*", "", ln['message'])
            target = re.sub(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", "", target)
            sentence = ln['revision_hash'] + ', '
            sentence += target.replace('\n', '').replace(',', '').strip() + ', '
            label_vector = [int(ln['labels'][x]) for x in labels]
            #print(label_vector)
            if sum(label_vector) == 1:
                sentence += str(label_vector.index(1))
                f.write(sentence + '\n')

if __name__ == "__main__":
    # host & port info
    host = "localhost"
    port = 27017
    
    # Database system, collection(table), target field
    db_name = "smartshark_1_1"
    table_name = "commit"
    target_fields = ["revision_hash", "labels", "message"]
    
    # Set connection & Get client instance
    client = MongoClient(host, port)
    
    # Path & target repos info
    base_path = Path(__file__).parent.parent.parent
    # repo_list = listdir(str(base_path.resolve()) + '/Repos')
    
    # Process
    result = find_from_mongo(client, db_name, table_name, {}, target_fields)
    create_csv(result)
