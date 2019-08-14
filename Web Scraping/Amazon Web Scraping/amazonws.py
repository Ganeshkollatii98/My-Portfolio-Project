# Amazon webscraping 
# In this project searching a product name and downloading the images
# Here i used Library as BeautifullSoap
# browser requests
# Pandas is using for DataFrame 
import bs4
import requests as rq
import os
import pandas as pd
print("Enter a product to get details of it from amazon.")
"""
# product = input()
# s=rq.Session()
# header={'User_Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
# html_of_that_product_page = s.get('https://www.amazon.in/s?k='+product+'&ref=nb_sb_noss_2',headers=header)
header={'User-Agent':'Mozilla/5.0'}
"""
product = input()
html_of_that_product_page = rq.get('https://www.amazon.in/s?k='+product+'&ref=nb_sb_noss_2',headers=header)

#html_of_that_product_page.text ---- converting raw text of html page to soup object
soupob = bs4.BeautifulSoup(html_of_that_product_page.text,'html.parser')

print(soupob.title)
print(soupob.title.text)

results = soupob.findAll(class_='s-result-item')
products = []
for i in results:
    if i.find(class_='a-size-base-plus') != None:
        itemname = i.find(class_='a-size-base-plus').text
    else:
        itemname = i.find(class_='a-size-medium')
    if i.find(class_='a-price-whole') != None:
              itemprice = i.find(class_='a-price-whole').text
    else:
              itemprice = i.find(class_='a-color-price')
    itemimage = i.find('img')['src']
    products.append([itemname,itemprice,itemimage])
print(len(results))
# print(results[0].findAll(class_='a-size-base-plus'))
# print(products)
os.mkdir(product)
#item_list=pd.DataFrame({'itemsnames':itemname,'Prizes':itemprice})
#print(item_list)        
print(products)

#storeing the image data by folder
for index,link in enumerate(products):
	imgdata = rq.get(link[2]).content
	with open(product+'\\'+str(index+1)+'.jpg','wb+') as f:
		f.write(imgdata)
