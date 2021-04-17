#读取text.txt文件内容
fp1 = open('text.txt', 'r', encoding='utf-8')  #只读
content_read = fp1.read()
print(content_read)
fp1.close()  #关闭文件！
