import requests
from bs4 import BeautifulSoup

ITEMS = 100
URL = f'https://hh.ru/search/vacancy?text=%D1%84%D0%B8%D0%BD%D0%B0%D0%BD%D1%81%D0%BE%D0%B2%D1%8B%D0%B9+%D0%BC%D0%B5%D0%BD%D0%B5%D0%B4%D0%B6%D0%B5%D1%80&items_on_page={ITEMS}'
headers = {
    "accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"}


def extract_max_page():

  pages = []
  hh_request = requests.get(URL, headers=headers)
  hh_soup = BeautifulSoup(hh_request.text, 'html.parser')

  paginator = hh_soup.find_all("span", {'class': 'pager-item-not-in-short-range'})

  for page in paginator:
    pages.append(int(page.find('a').text))

  return pages[-1]


def extract_hh_jobs(last_page):
  jobs=[]
  #for page in range(last_page):

  result = requests.get(f'{URL}&page=0', headers=headers)
  print(result.status_code)

  soup = BeautifulSoup(result.text, 'html.parser')
  results = soup.find_all('div', {'class':'vacancy-serp-item-body__main-info'})
  for result in results:
    title = result.find('a').text
    company = result.find('div', {'class': 'vacancy-serp-item-company'}).find('a').text
    print(company)
  return jobs