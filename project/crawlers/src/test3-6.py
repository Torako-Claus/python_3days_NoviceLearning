'''
Created on 2021年4月17日
    读取(load)a.json，将a.json字符串加载为对象(loads)
@author: Torako
'''
import json
# with open('a.JSON', 'r', encoding='utf-8') as fp:
#     json_str = json.load(fp)
#     fp.close()
# print(json_str)
# print(type(json_str))  #读取出来就是list类型

json_str2 = '[{"name": "小王", "score": 95}, {"name": "小明", "score": 99}, {"name": "小黄", "score": 98}]'  #JSON格式文件只有双引号
books = json.loads(json_str2)
print(type(books), books)
    