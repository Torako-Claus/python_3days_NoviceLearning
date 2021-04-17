'''
Created on 2021年4月16日
    计算正方形/圆形的面积
@author: Torako
'''

a = int(input("请输入正方形边长："))
b = a ** 2

print("边长为", a, "的正方形的面积为", b)  #print中不同类型的数据不能用+链接打印

r = float(input("请输入圆半径："))
S = 3.14159 * r ** 2

print("半径为", r, "的圆的面积为", S)