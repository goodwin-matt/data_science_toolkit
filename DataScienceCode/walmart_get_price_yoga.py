import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://www.walmart.com/ip/Life-Energy-5mm-EkoSmart-Cork-Yoga-Mat-with-Yoga-Strap/565236292')
soup = BeautifulSoup(page.text, 'html.parser')
test =soup.find_all('span', class_="price-group")
m = test[0]
price = float(str(m.get('aria-label'))[1:])

fields=[price]
with open('yoga_mat.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
