# Weather Forecast 
# From this website https://forecast.weather.gov/
# Day wise temprature form this website
# Using Pandas storeing in excel sheet 
from bs4 import BeautifulSoup as b
import requests as req
import pandas as pd

url_data=req.get("https://forecast.weather.gov/MapClick.php?lat=40.6792&lon=-85.7019#.XQkYhy3hXDc")
soup=b(url_data.text,'html.parser')
linksaslist=soup.select('a')
week=soup.findAll(id='seven-day-forecast-body')
items=soup.findAll(class_='tombstone-container')

period_names=[item.find(class_='period-name').get_text() for item in items]

short_desc=[item.find(class_='short-desc').get_text() for item in items]

temp=[item.find(class_='temp').get_text() for item in items]



weather_report=pd.DataFrame({'period':period_names,'short-description':short_desc,'temprature':temp})
print('-----------------------------------------------------')
print(weather_report)
weather_report.to_csv('weather2.csv')