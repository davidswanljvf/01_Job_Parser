# Импортируем функции из headhunter.py
from headhunter import extract_max_page, extract_hh_jobs

hh_max_page = extract_max_page()  # Получаем максимальное количество страниц с объявлениями о вакансиях
hh_jobs=extract_hh_jobs(hh_max_page)  # Извлекаем данные о вакансиях с указанного количества страниц
print(hh_jobs)
