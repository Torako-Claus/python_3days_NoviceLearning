'''
Created on 2021年4月17日
    将字典和列表转换为JSON数据
@author: Torako
'''
import json

users = [
    {
        'name':'小王',
        'score':95
        },
    {
        'name':'小明',
        'score':99
        },
    {
        'name':'小黄',
        'score':98
        }
    ]
json_str = json.dumps(users, ensure_ascii=False)
print(json_str)