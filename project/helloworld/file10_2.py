'''
Created on 2021年4月16日
    计算消费税和折扣
@author: Torako
'''
#增值税为19%
VAT = 0.19
price_before_discount = float(input("请输入产品原价："))
discount = int(input("请输入折扣（0-100）："))

discount_amount = price_before_discount * discount / 100  #折后价

price_after_discount = price_before_discount - discount_amount
sales_tax = price_after_discount * VAT
price_after_tax = discount_amount + sales_tax

print("税后价为", price_after_tax)
