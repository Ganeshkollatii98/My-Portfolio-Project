import bs4 
import requests as req
import os
import pandas as pd
itemname=input('search item name only mobiles and Laptops')
budget=input('Enter your budget')
url_data=req.get('https://www.flipkart.com/search?q='+itemname+'%20under%20'+budget+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
data=bs4.BeautifulSoup(url_data.text,'html.parser')
#print(data.title.text)
container=data.findAll(class_='_1UoZlX')
item_name=data.findAll(class_='_3wU53n')
specifications=data.findAll(class_='_3ULzGw')
print("********* TOP FIVE SPECIFICATIONS************")
for i in specifications[0:4]:
    print(i.get_text(),'\n')
    
price1=[]
price=data.findAll(class_='_1vC4OE _2rQ-NK')
for i in price:
    price1.append(i.get_text())
price1


    
item=[]
for i in item_name:
    item.append(i.get_text())

item_list=pd.DataFrame({'Laptops':item,'Prizes':price1})
print(item_list)
name=str(budget)
item_list.to_csv(itemname)