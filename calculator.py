# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:41:21 2020

@author: Gauri
"""


class Calculator:
    
    def getInput(self):
        num1=int(input("Enter first number."))
        num2=int(input("Enter second number."))
        return num1,num2
    
    def addition(self,num1,num2):
        return num1+num2
    
    
    def subtraction(self,num1,num2):
        return num1-num2
    
    def multiplication(self,num1,num2):
        return num1*num2
    
    def division(self,num1,num2):
        return num1//num2
    
    
    
    

    
    

def main():
    o=Calculator()
    
    flag=1
    
    while flag:
        print("1:Addition")
        print("2:Subtraction")
        print("3:Multiplication")
        print("4:Division")
        print("5:Exit")
        choice=int(input("Enter your choice."))
        
    
        if choice==1:
            num1,num2=o.getInput()
            result=o.addition(num1,num2)
            print("Result of additon is ",result)
        
        elif choice == 2:
            num1,num2=o.getInput()
            result=o.subtraction(num1,num2)
            print("Result of subtraction is ",result)
        
        elif choice == 3:
            num1,num2=o.getInput()
            result=o.multiplication(num1,num2)
            print("Result of multiplication is ",result)
        
        elif choice == 4:
            num1,num2=o.getInput()
            try:
                result=o.division(num1,num2)
                print("Result of division is ",result)
            
            except ZeroDivisionError:
                print("ZeroDivisionError:Cannot divide by zero.")
            
            
        elif choice == 5:
            flag=0
            
        else:
            print("Enter valid choice.")
    
    
    
    
main()