'''
Created on 2021年4月17日
    将json数据dump到文件中
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
with open('a.JSON', 'w') as fp:
    json.dump(users, fp)