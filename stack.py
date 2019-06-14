# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 05:08:19 2019

@author: Jiastin
"""
#STACK
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return (len(self.items))
        
from pythonds.basic.stack import stack
s=stack()
print(s.isEmpty())
s.push(4)
s.push("Arsenal")
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(5.3)
print(s.pop())
print(s.pop())
print(s.size())

#simple balanced parentheses
#from pythonds.basic.stack import stack
def parChecker(symbolString):
    s=stack()
    balanced=True
    index=0
    while index<len(symbolString) and balanced:
        symbol=symbolString[index]
        if symbol=="(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=false
            else:
                s.pop()
    index+=index
    if balanced and s.isEmpty():
        return true
    else:
        return false
#general balanced symbols
#from pythonds.basic.stack import stack
def parCheck(symbolString):
    s=stack()
    balanced=True
    index=0
    while balanced and index<len(symbolString):
        symbol=symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=false
            else:
                top=s.pop()
                if not matches(top,symbol):
                    balanced=false
    if balanced and s.isEmpty():
        return true
    else:
        return false
def matches(a,b):
    return '([{'.index(a)==')]}'.index(b)

#decimal converter
#from pythonds.basic.stack import stack
remStack=stack()
def dectrans(decNumber):
    while decNumber>0:
        rem=decNumber%2
        remStack.push(rem)
        decNumber=decNumber//2
        binString=''
    if not remStack.isEmpty():
        binString=binString+str(remStack.pop())
    return binString
#decimal converter (general)    
#from pythonds.basic.stack import stack
remStack=stack()
def dectrans(decNumber,base):
    while decNumber>0:
        rem=decNumber%base
        remStack.push(rem)
        decNumber=decNumber//base
        binString=''
    if not remStack.isEmpty():
        newString=newString+str(remStack.pop())
    return newString
print(dectrans(25,2))
print(dectrans(25,16))

from pythonds.basic.stack import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

        