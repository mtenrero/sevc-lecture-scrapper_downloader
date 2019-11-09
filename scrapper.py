import requests
import urllib.request
import time
from bs4 import BeautifulSoup

from downloadDocuments import DownloadDocuments

url = 'https://sevc2019.com/index.php/es/programa-cientifico/anestesia-y-control-del-dolor'

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

categoriesMenuList = soup.find('ul', 'nav menu').find_all('li')

print("Scrapping contents...")

for category in categoriesMenuList:

    categoryName = category.a.string
    categoryLink = 'https://sevc2019.com{}'.format(category.a.get('href'))
    print("Accesing category: {}...".format(categoryName))

    categoryResponse = requests.get(categoryLink)
    soupCategory = BeautifulSoup(categoryResponse.text, "html5lib")

    items = soupCategory.find('table').find('tbody').find_all('tr')
    print('Succesfully detected items')

    for item in items:
        itemName = item.find('td').find('a').find('span').next.string
        itemLink = 'https://sevc2019.com{}'.format(item.find('td').find('a').get('href'))
        print('Retrieving item {}...'.format(itemName))

        DownloadDocuments().download(itemLink, categoryName)

    
print("All contents has been succesfully scrapped & downloaded! :)")