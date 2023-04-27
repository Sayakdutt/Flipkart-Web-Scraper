import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml
import openpyxl


num_pages = int(input("Enter number of pages to scrape: "))

Product_name = []
Prices = []
Descriptions = []
Reviews = []

for i in range(1,num):
    url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+ str(i)
    try:
        r = requests.get(url,timeout=5)
        soup = BeautifulSoup(r.text,"lxml")
        box = soup.find("div",class_="_1YokD2 _3Mn1Gg")
        
        names = box.find_all("div",class_="_4rR01T")
        for i in names:
            name = i.text
            Product_name.append(name)
            
        prices = box.find_all("div",class_="_30jeq3 _1_WHN1")
        for i in prices:
            price = i.text
            Prices.append(price)
            
        desc = box.find_all("ul",class_="_1xgFaf")
        for i in desc:
            name = i.text
            Descriptions.append(name)
            
            
        reviews = box.find_all("div",class_="_3LWZlK")
        for i in reviews:
            review = i.text
            Reviews.append(review)
            
    except requests.exceptions.ConnectTimeout:
        print("Request to", urls, "timed out")
        
df = pd.DataFrame({"Product Name":Product_name,"Prices": Prices, "Product Description": Descriptions , "Reviews": Reviews})
df.to_excel("flipkart_mobile_under_50000.xlsx",index=False)