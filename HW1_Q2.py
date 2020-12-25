#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 10:56:17 2020

@author: basakulcay
"""

#A company pays its employees as pieceworkers (who work on only one type of item and
#receive a fixed amount of money for each of the items they produce), commission workers
#(who receive $300 plus 6% of their gross weekly sales), hourly-workers (who receive a
#fixed hourly wage up to the first 40 hours they work and 1.25 times their hourly wage for
#overtime hours worked), and managers (who receive a fixed weekly salary). Write a
#program to compute the weekly pay for each employee. You do not know the number of
#the employees in advance. Each type of employee has its own pay-code: Pieceworkers
#have pay-code 1, commission workers have pay-code 2, hourly-workers have a pay-code
#3, and managers have a pay-code 4. Prompt the user to enter the pay-code (-1 to end) of
#the employee and appropriate facts your program needs to calculate the employee’s
#weekly pay. Print for each entry, the calculated weekly pay of that employee. At the end
#(when user enters -1), display the total weekly pay for all and the total number of
#employees for each type.


payCode=float(input("Enter the pay-code (enter -1 to end): "))

while payCode>0:

    if payCode==1:
        numItems=float(input("Enter number of pieceworks per week: "))
        pieceCost=float(input("Enter the amount needs to be paid to the employee for each piece: "))
        pay1=numItems*pieceCost
        print("The weekly amount that needs to be paid to the employee: ",pay1,"dollars")
        payCode=float(input("Enter the pay-code (enter -1 to end): "))
        
    if payCode==2:
        grossWeekly=float(input("Enter the gross weekly salary of the employee: "))
        commission=grossWeekly*0.06
        pay2=300+commission
        print("The weekly amount that needs to be paid to the employee: ",pay2,"dollars")
        payCode=float(input("Enter the pay-code (enter -1 to end): "))
    if payCode==3:
        normalPay=float(input("Enter the hourly pay-rate: "))
        overPay=normalPay*1.25
        hours=float(input("Enter the number of hours worked in a week: "))
        if hours>40:
            pay3=40*normalPay+(hours-40)*overPay
        else:
            pay3=hours*normalPay    
        print("The weekly amount that needs to be paid to the employee: ",pay3,"dollars")
        payCode=float(input("Enter the pay-code (enter -1 to end): "))
    if payCode==4:
        pay4=float(input("Enter the weekly salary for the manager: "))
        print("The weekly amount that needs to be paid to the employee: ",pay4,"dollars")
        payCode=float(input("Enter the pay-code (enter -1 to end): "))
        
    if payCode==-1:
        code1Emp=float(input("Enter the number of employees who got paid based on the number of pieceworks: "))
        code2Emp=float(input("Enter the number of employees who got paid commission-based: "))
        code3Emp=float(input("Enter the number of employees who got paid based on hourly rate: "))
        code4Emp=float(input("Enter the number of employees who got paid salary-based: "))
        
        payTotal=code1Emp*pay1+code2Emp*pay2+code3Emp*pay3+code4Emp*pay4
        
        
       
        

    
    
    
     