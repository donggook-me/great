from bson import json_util 
from ast_diff_src.python_get_ast import *
import ast
    
def get_json(file_name):
    with open(file_name, 'r') as file:
        completed = json_util.loads(file.read())
    file.close()
    return completed

def get_diffline_list(completed):
    diff_line_list = []
    for n, result in enumerate(completed):
        labels = result['lines_manual']
        first_labels = next(iter(labels.values()))
        diff_lines = []
        for cur_lines in first_labels.values():
            diff_lines.extend(cur_lines)
        diff_lines.sort()
        diff_line_list.append(diff_lines)
    return diff_line_list


def get_ast_lines(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return lines

def get_pyscript(file_name):
    with open(file_name, 'r') as file:
        files = file.readlines()
    file.close()
    return files

def node_diff_one_line_before_and_after(one_line_before_ast_node, one_line_after_ast_node):
    node_list = one_line_after_ast_node.copy()        
    for type_value_node in one_line_before_ast_node:
        for one_line_after_node in node_list:
            # print("type_value_node", type_value_node)
            if type_value_node.get("value"):
                if one_line_after_node["type"] == type_value_node["type"] and one_line_after_node["value"] == type_value_node["value"]:
                        node_list.remove(one_line_after_node)
                        break
            else:
                if one_line_after_node["type"] == type_value_node["type"]:
                    node_list.remove(one_line_after_node)
                    break
    return node_list
    

def ast_diff(reorder_list, diffline_list):    
    one_line_before = ''
    one_line_after = ''
    whole_line = ''
    diffline_list = diffline_list[0]
    while(diffline_list):
        diffline_num = diffline_list[0]
        print("dfn", diffline_num)
        diffline_list.pop(0)
        switch = False
        key = False 
        for line, line_num in reorder_list:
            line = "\n" + line
            if key:
                whole_line += line
                continue
            if switch:
                one_line_after += line
                whole_line += one_line_after
                key = True
                continue
            if line_num == diffline_num:
                one_line_after += line
                switch = True
                continue
            whole_line += line
            
            one_line_before += line
            one_line_after += line
            
            
        print("one_line_before_script", one_line_before)
        print("one_line_after_script", one_line_after)
        # print("whole_line_script", whole_line)    
        
        # print("break", main_get_ast(whole_line))
        print("one_line_before", main_get_ast(one_line_before))
        
        one_line_before_ast_node = eval(main_get_ast(one_line_before)[0])
        print()
        one_line_after_ast_node = eval(main_get_ast(one_line_after)[0])
        # whole_line_ast_node = eval(main_get_ast(whole_line)[0])
        
        node_list = node_diff_one_line_before_and_after(one_line_before_ast_node, one_line_after_ast_node)
        
        # node_list_one_line_before = node_diff_one_line_before_and_after(one_line_before_ast_node, whole_line_ast_node)
        # node_list_one_line_after = node_diff_one_line_before_and_after(one_line_after_ast_node, whole_line_ast_node)
        
        # node_list = node_diff_one_line_before_and_after(node_list_one_line_before, node_list_one_line_after)

        # print("one_line_before", node_list_one_line_before)
        print()
        # print("one_line_after", node_list_one_line_after)    
            
        for i in node_list:
            print("node_list", i, "\n")

        return node_list

            
        
        
    

if __name__ == '__main__':
    
    #1 get diff_line_list from test_labels.json(I made it myself for test)
    json_file = get_json("/Users/dongguk/Git/replication-kit-2020-line-validation/data/test_labels.json")
    diffline_list = get_diffline_list(json_file)
    
    #2 In advance, I used "get_ast.py" to convert python_code2.txt into train_ast.txt
    ast_file = get_ast_lines("/Users/dongguk/Git/M2TS/M2TS/Data_pre/train_ast.txt")
    # reorder_list  = reordering_script_module.src.main.main("/Users/dongguk/Git/reordering_script_module/inputs/a.py")
    
    
    



            

            


