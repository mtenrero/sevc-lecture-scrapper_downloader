import requests
import urllib.request
import time
from bs4 import BeautifulSoup

import os

class DownloadDocuments:

    def makeCategoryDir(self, category: str):
        path = "./contents/{}".format(category)

        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)
    
    def download(self, url: str, parentCategory: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.find('div', 'page-header').find('h2').string.strip()
        pdfIcon = soup.find('li', 'pdf-icon')

        if pdfIcon is not None:
            downloadPDFLink = soup.find('li', 'pdf-icon').a.get('href')

            filename = downloadPDFLink.rsplit('/', 1)[1]

            self.makeCategoryDir(parentCategory)

            r = requests.get(downloadPDFLink, allow_redirects=True)
            open("./contents/{}/{}".format(parentCategory, filename), 'wb').write(r.content)