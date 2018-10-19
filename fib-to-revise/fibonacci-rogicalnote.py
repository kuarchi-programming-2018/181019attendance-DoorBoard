# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:57:19 2018

@author: Takuto
"""
def fib(n):
    if n >= 2:
        a = 0
        b = 1
        for i in range(n - 1):
            a,b = b,a+b
        return b
    elif n == 1:
        return 1
    else:
        return 0
print(fib(2018))


print(fib(5))


#処理が重かったため修正しました。