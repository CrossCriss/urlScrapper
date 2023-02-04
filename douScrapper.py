import requests
import json
from bs4 import BeautifulSoup

# with open('dou.html', 'r', encoding='utf-8') as f:
#     html = f.read()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}

# soup = BeautifulSoup(html, 'lxml')
# all_companys_hrefs = soup.find_all('a', class_='company-name')

# all_companys_dict = {}
# for company_href in all_companys_hrefs:
#     company_name = company_href.text
#     all_companys_hrefs = company_href.get('href')

#     all_companys_dict[company_name] = all_companys_hrefs

with open("all_companys_dict.json",encoding='utf-8') as f:
    all_companys_dict = json.load(f)

# for company_name, company_href in all_companys_dict.items():
#     response = requests.get(url=company_href, headers=headers).text

#     with open(f'companys/{company_name}.html', 'w', encoding='utf-8') as f:
#         f.write(response)

#     with open(f'companys/{company_name}.html', encoding='utf-8') as f:
#         src = f.read()
    
#     soup = BeautifulSoup(src, 'lxml')
#     company_link = soup.find('a', class_='site').get('href')
#     print(company_name, company_link)


for company_name, company_href in all_companys_dict.items():
    with open(f'companys/{company_name}.html', encoding='utf-8') as f:
        src = f.read()
    soup = BeautifulSoup(src, 'lxml')
    try:
        company_link = soup.find(class_ = 'site').find('a').get('href')
    except:
        company_link = 'None'

    with open('companys_links.txt', 'a', encoding='utf-8') as f:
        f.write(f'{company_name} - {company_link}\n')

