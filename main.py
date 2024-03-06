# Импортируем функции из headhunter.py
from headhunter import extract_max_page, extract_hh_jobs

max_page = extract_max_page()  # Получаем максимальное количество страниц с объявлениями о вакансиях

extract_hh_jobs(max_page)  # Извлекаем данные о вакансиях с указанного количества страниц
