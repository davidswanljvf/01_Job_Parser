# Импортируем необходимые модули
import requests  # Модуль для выполнения HTTP-запросов
from bs4 import BeautifulSoup  # Модуль для парсинга HTML-контента

# Устанавливаем константы
ITEMS = 100  # Количество элементов на странице
URL = f'https://hh.ru/search/vacancy?&search_field=name&search_field=company_name&search_field=description&text=%D1%84%D0%B8%D0%BD%D0%B0%D0%BD%D1%81%D0%BE%D0%B2%D1%8B%D0%B9+%D0%BC%D0%B5%D0%BD%D0%B5%D0%B4%D0%B6%D0%B5%D1%80&items_on_page={ITEMS}'
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
}  # Заголовки для HTTP-запроса

# Функция для извлечения максимального количества страниц с объявлениями о вакансиях
def extract_max_page():
    pages = []  # Список для хранения номеров страниц
    hh_request = requests.get(URL, headers=headers)  # Отправляем GET-запрос на URL с заданными заголовками
    hh_soup = BeautifulSoup(hh_request.text, 'html.parser')  # Создаем объект BeautifulSoup для парсинга HTML-страницы

    paginator = hh_soup.find_all("span", {'class': 'pager-item-not-in-short-range'})  # Находим все элементы с номерами страниц

    for page in paginator:  # Перебираем найденные страницы
        pages.append(int(page.find('a').text))  # Добавляем номер страницы в список

    return pages[-1]  # Возвращаем последнюю страницу (максимальное значение)

def extract_job(html):
  title = html.find('a').text
  company = html.find('div', {'class': 'vacancy-serp-item-company'}).find('a').text
  company = company.strip()
  location = html.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text
  location = location.partition(',')[0]
  
  return{'title': title, 'company':company, 'location': location}

# Функция для извлечения объявлений о вакансиях с указанной страницы
def extract_hh_jobs(last_page):
    jobs = []  # Список для хранения данных о вакансиях

    result = requests.get(f'{URL}&page=0', headers=headers)  # Отправляем GET-запрос на первую страницу с заданными заголовками
    print(result.status_code)  # Выводим статус код ответа сервера

    soup = BeautifulSoup(result.text, 'html.parser')  # Создаем объект BeautifulSoup для парсинга HTML-страницы
    results = soup.find_all('div', {'class':'vacancy-serp-item-body__main-info'})  # Находим все объявления о вакансиях

    for result in results:  # Перебираем найденные объявления
        job=extract_job(result)
        jobs.append(job)
    return jobs  # Возвращаем список с данными о вакансиях
