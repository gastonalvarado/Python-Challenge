# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 17:46:02 2019

@author: gasto
"""
import os #importing operating system module
import csv #importing csv module

file = os.path.join("budget_data.csv") #open CSV File
with open(file) as csvfile:
   
    reader=csv.reader(csvfile,delimiter=',')  #Establish the reader and delimit the data
   
    months=0  #Establish Variable for counting months
    revenue=0  #Establish variable for adding revenue
   
    rows=[r for r in reader]  # Count the Total number of Rows
    
    change_in_revenue=int(rows[1][1]) #Start count in the first Value available in the Sheet
    max = rows[1]
    min=rows[1]  
    
    for i in range(1,len(rows)): #Looping through Data
        
        months=months+1 #Establishing the counter for months
        row=rows[i]     
        revenue= int(row[1]) + revenue #Calculating revenue
            
        if i > 1: #Excluding Header Row
            change_in_revenue=change_in_revenue + int(row[1])-int(rows[i-1][1])
        
        if int(max[1]) < int(row[1]): #Finding Max Revenue
            max=row
       
        if int(min[1]) > int(row[1]):  #Finding Min Revenue
            min=row

average= int(revenue /months) #Calculating Average
average_change_in_revenue=int(change_in_revenue/months) #Average Change in Revenue

#Printing all the answers

print("Financial Analysis")
print("=====================================================")
print("Total Months: " + str(months))
print("Total Revenue: " +"$" +str(revenue))       
print("Average Revenue Change: " +"$"+ str(average))
print("Average Change in Revenue Change: " +"$"+ str(average_change_in_revenue))
print("Greatest Increase in Revenue:" + str(max[0])+" ($" + str(max[1])+")")
print("Greatest Decrease in Revenue:" + str(min[0])+" ($" + str(min[1])+")")