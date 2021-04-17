'''
Created on 2021年4月17日

@author: Torako
'''
#将指定内容写入text2.txt文件
fp2 = open('text2.txt', 'w')
content_write = '这是我自己写得一行......'
fp2.write(content_write)  #将内容写入

fp2 = open('text2.txt', 'r')
content_read = fp2.read()
print(content_read)
fp2.close()