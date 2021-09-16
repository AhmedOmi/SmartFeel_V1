import bs4
import requests
import shutil

"""
function scraping data from google url
it's a function to scraping what images you want
"""

Url = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'


def scraping(data, quantity):
    URL_input = Url + 'q=' + data
    print('Fetching from url =', URL_input)
    URLdata = requests.get(URL_input)
    bs = bs4.BeautifulSoup(URLdata.text, "html.parser")
    IMG = bs.find_all('img')
    i = 0
    while i < quantity:
        for link in IMG:
            try:
                images = link.get('src')
                ext = images[images.rindex('.'):]
                if ext.startswith('.png'):
                    ext = '.png'
                elif ext.startswith('.jpg'):
                    ext = '.jpg'
                elif ext.startswith('.jfif'):
                    ext = '.jfif'
                elif ext.startswith('.com'):
                    ext = '.jpg'
                elif ext.startswith('.svg'):
                    ext = '.svg'
                data = requests.get(images, stream=True)
                filename = str(i) + ext
                with open(filename, 'wb') as file:
                    shutil.copyfileobj(data.raw, file)
            except:
                pass
        i = i + 1
    print('\t\t\t good Job\t\t ')


data = input('Photos you want to scrape ?')
quantity = int(input('How many photos you want? '))

scraping(data, quantity)
