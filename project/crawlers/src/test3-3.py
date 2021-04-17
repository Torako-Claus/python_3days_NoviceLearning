'''
Created on 2021年4月17日

@author: Torako
'''

#按行读取文件内容
fp3 = open('text.txt', 'r', encoding='utf-8')
list_read = fp3.readlines()  #将文件按行读取到列表
for l in list_read:
    print(l + "\n")
fp3.close()