# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 19:55:42 2023

@author: Madhumitha
"""

# data collection
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("\n")

print("\t -- DATA COLLECTION --\t")
df=pd.read_csv(r"C:\Documents\data.csv")
print(df)

print("\n")
print("\n")

print("1. Number of rows and columns:")
print(df.shape) #no.of.rows and no.of.columns
print("\n")
print("2. Information about the data:")
print(df.info()) #information and describes the datatype of the record


print("\n")
print("\n")

#data mining
print("\t -- DATA MINING -- \t")
a= df.SEM_1
b=df.SEM_2
c=df.UG
d=df.ATTD
print("SEM_1:") #printing sem-1 records
print(a)
print("SEM_2:") #printing sem-2 records
print(b)
print("UG") #printing sem-1 records
print(c)
print("ATTENDANCE") #printing sem-2 records
print(d)


print("\n")
print("\n")

#data preprocessing
print("\t -- DATA PREPROCESSING -- \t")

print(" Data Cleaning:")
print(df.isnull()) #data cleaning

print("\n")
print("\n")

print("\t -- EXPLORATORY DATA ANALYSIS -- \t")

print("1. Mean:") #mean
print(a.mean()) #mean of sem-1
print(b.mean()) #mean of sem-2
print(c.mean()) #mean of UG
print(d.mean()) #mean of attendance
print("\n")

print("2. Median:") #median
print(a.median()) #median of sem-1
print(b.median()) #medianof sem-2
print(c.median()) #median of UG
print(d.median()) #median of attendance
print("\n")

print("\n")

print("3. Mode:") #mean
print(df.mode()) #mode of the data

print("\n")
print("\n")

print("\t -- DATA VISUALIZATION -- \t")

a= df.SEM_1
b=df.SEM_2
c=df.UG
d=df.ATTD
e=df.SUBJECT


m1=[a.mean(),b.mean(),c.mean(),d.mean()]
m2=[a.median(),b.median(),c.median(),d.median()]


#scatter plot
plt.scatter(x=a,y=b,color="blue",marker="o",s=100,alpha=0.5)
plt.scatter(x=c,y=d,color="green",marker="^",s=100,alpha=0.5)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Scatter Plot")
plt.show()


#line chart
plt.plot(m2,m1,color='#ff0090',marker='*')
plt.xlabel("median of data")
plt.ylabel("mode of data")
plt.title("Line Chart")
plt.show()


#bar chart
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8)) 
br1 = np.arange(len(e)) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 
plt.bar(br1, a, color ='#800080', width = barWidth, edgecolor ='grey', label ='Sem-1') 
plt.bar(br2, b, color ='#78184a', width = barWidth, edgecolor ='grey', label ='Sem-2') 
plt.bar(br3, c, color ='#6f00ff', width = barWidth, edgecolor ='grey', label ='UG') 
plt.xlabel('SEMESTER', fontweight ='bold', fontsize = 15) 
plt.ylabel('ATTENDANCE', fontweight ='bold', fontsize = 15) 
plt.xticks([r + barWidth for r in range(len(e))], ['Sub1', 'Sub2', 'Sub3', 'Sub4', 'Sub5'])
plt.legend()
plt.show() 


#piechart
y = m1
mylabels = ["Sem1", "Sem2", "UG", "Attendance"]
mycolors = ["#d4af37", "#ff6700", "#e62020", "#fff000"]
plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 
