'''
Created on 2021年4月17日
    自定义函数综合处理CSV文件
@author: Torako
'''
import csv
# 读取文件 函数
def read_csv():
    with open('', 'r') as fp:
        reader = csv.reader(fp)
        titles = next(reader)  #title迭代掉第一行表头
        for x in reader:
            print(x)

# 通过字典读取文件
def read_csv_dict():
    with open('', 'r') as fp:
        reader = csv.DictReader(fp)
        next(reader)
        for x in reader:
            value = {
                'name':x['name'],
                'other':x['other']
                }
            print(value)

# 写入文件
def write_csv():
    headers = ['name', 'price', 'author']
    values = [
        ('流浪地球',18,'刘慈欣'),
        ('梦的解析',30,'弗洛伊德'),
        ('时间简史',35,'斯蒂芬·霍金')
        ]
    with open('book.csv', 'w', encoding='utf-8-sig', newline='') as fp:  # newline是写入一行后做的事
        writer = csv.writer(fp)
        # 写入表头
        writer.writerow(headers)  # 单行写入
        # 写入数据
        writer.writerows(values)  # 多行写入

# 通过字典写入数据
def wirter_csv_dict():
    headers = ['username', 'age', 'height']
    values = [
        {
            'username':'张三',
            'age':35,
            'height':178
         },{
             'username':'李四',
             'age':27,
             'height':182
         },{
             'username':'王五',
             'age':23,
             'height':180
             }
         ]
    
    with open('classroom.csv', 'w', encoding='utf-8-sig', newline='') as fp:
        writer = csv.DictWriter(fp, headers)  # 根据headers初始化对象
        writer.writerows(values)  
        
        