import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://www.walmart.com/ip/Original-Boppy-Nursing-Pillow-and-Positioner-Love-Letters/47714896')
soup = BeautifulSoup(page.text, 'html.parser')
test =soup.find_all('span', class_="price-group")
m = test[0]
price = float(str(m.get('aria-label'))[1:])

fields=[price]
with open('boppy_price.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
