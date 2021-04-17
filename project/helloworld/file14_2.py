'''
Created on 2021年4月16日
    切片/逆序显示字符串
@author: Torako
'''
a = "Hello World"

print(a[7:9])  #It displays a[7]=o and a[9]=r.
print(a[4:10:2])  #step=2, it displays a[4], a[6] and a[8].
print(a[7:])  #It displays from a[7] to the end.
print(a[:3])  #It displays first three letters.

print(a[3:-2])  #It displays from a[3] to a[-3] = "lo Wor". 有左无右边
print(a[-4:-2])  #It displays from a[-4] to a[-3] = "or". 有左无右边
print(a[-3:])  #It displays last 3 letters.
print(a[:-3])  #It displays from a[0] to a[-4] = "Hello Wo". 有左无右边

s = input("请任意输入一句话：")
print(s[::-1])
