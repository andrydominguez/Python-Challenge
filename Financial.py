
# coding: utf-8

# The total number of months included in the dataset
# 
# The net total amount of "Profit/Losses" over the entire period
# 
# The average of the changes in "Profit/Losses" over the entire period
# 
# The greatest increase in profits (date and amount) over the entire period
# 
# The greatest decrease in losses (date and amount) over the entire period

# In[1]:


import os
import csv

csv_path= os.path.join("Resources","budget_data.csv")

with open(csv_path,'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    
    #the total number of months included in the dataset
    total_months = 0
    net_total = 0
    changes = []
    difference = []
    changes_months = []
    
    for i in csvreader:
        total_months = total_months + 1 
        net_total = net_total + int(i['Profit/Losses'])
        changes.append(int(i['Profit/Losses']))
        changes_months.append(i['Date'])
    i=1
    while i < len(changes):
        diff = changes[i] - changes[i-1]
        difference.append(diff)
        i = i+1
        
    mean = sum(difference)/len(difference)  
    max_increase = max(difference)
    min_increase = min(difference)
    


# In[2]:


with open(csv_path,'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    
    connect = zip(changes_months[1:],difference)
    for i in connect:
        if i[1] == max_increase:
            date_increase = i[0]
        if i[1] == min_increase:
            date_decrease = i[0]
        
        


# In[3]:


print(f"Financial Analysis:")
print("-------------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total Revenue: {net_total} USD")
print(f"Average Revenue Change: {mean} USD")
print(f"Greatest Increase in Profits: {date_increase} {max_increase} USD")
print(f"Greatest Decrease in Profits: {date_decrease} {min_increase} USD")
print("")
   



# In[4]:


with open("Financial Analysis.txt",'w') as filewriter:     
    filewriter.write(f"Financial Analysis:\n")
    filewriter.write("-------------------------------------------------------\n")
    filewriter.write(f"Total Months: {total_months}\n")
    filewriter.write(f"Total Revenue: {net_total} USD\n")
    filewriter.write(f"Average Revenue Change: {mean} USD\n")
    filewriter.write(f"Greatest Increase in Profits: {date_increase} {max_increase} USD\n")
    filewriter.write(f"Greatest Decrease in Profits: {date_decrease} {min_increase} USD\n")
   
    

