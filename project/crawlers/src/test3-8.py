'''
Created on 2021年4月17日
    Read CSV file(csv.reader)/Get CSV file by titles(csv.DictReader).
@author: Torako
'''
import csv
with open('data.csv', 'r', encoding='utf-8-sig') as fp:
    # reader = csv.reader(fp)
    # # titles = next(reader)  #titles依次拿走reader的值|注意reader的缩进问题
    # for x in reader:
    #     print(x)
        
    reader = csv.DictReader(fp)
    titles = next(reader)
    for x in reader:
        print(x['author'], end='\t')
        print(x['name'], end='\t')
        print(x['price'])