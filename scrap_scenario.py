import bs4
from bs4 import BeautifulSoup
import requests

output_list = []

def scraping(webpage, page_number):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    next_page = webpage + str(page_number) + '.html'
    response = requests.get(str(next_page), headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup_content = soup.findAll('div', attrs={'class': 'grid-inner col-inner clearfix'})

    for x in range(len(soup_content)):
        
        #print("https://www.theedgemarkets.com" + soup_content[x].find('a')['href'])
        link = "https://www.theedgemarkets.com " + soup_content[x].find('a')['href']

        #print(soup_content[x].find('span', attrs={'class': 'field-content'}).text)
        upload_date = soup_content[x].find('span', attrs={'class': 'field-content'}).text

        if soup_content[x].findAll('div', attrs={'class': 'field-content'})[1].text != '':
            #print(soup_content[x].findAll('div', attrs={'class': 'field-content'})[1].text)
            tag = soup_content[x].findAll('div', attrs={'class': 'field-content'})[1].text
        else:
            #print('N/A')
            tag = 'N/A'

        #print(soup_content[x].findAll('span', attrs={'class': 'field-content'})[1].text)
        title = soup_content[x].findAll('span', attrs={'class': 'field-content'})[1].text

        news_info = { 
            'link': link, 
            'upload_date' : upload_date, 
            'tag' : tag,
            'title' : title
        }

        output_list.append(news_info)

    return output_list
        
output = scraping('https://www.theedgemarkets.com/categories/corporate?page=', 1)
#print(output)
