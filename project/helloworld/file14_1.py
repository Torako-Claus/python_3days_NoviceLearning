'''
Created on 2021年4月16日
    计算三位数中每位数字的总和
@author: Torako
'''
a = int(input("请输入一个三位数："))

digit1, digit2, digit3 = str(a)  ##直接拆分
print(digit1, digit2, digit3)

total = int(digit1) + int(digit2) + int(digit3)
print(total)