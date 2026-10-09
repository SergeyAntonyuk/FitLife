# Проект FitLife - MVP версия 1.0


# 1. Знакомство
print('Приветствую! Я твой фитнес-бот. Давай знакомиться?')
print('Введи свои данные ниже.')
# Узнаем у пользователя имя и сохраняем в переменную user_name
user_name = input('Твое имя: ')
# Узнаем возраст и сохраняем в переменную user_age (преобразовываем в число)
user_age = int(input('Твой возраст: '))

# 2. Сбор данных
# Запрашиваем вес (в кг) и сохраняем в user_weight (тип float)
user_weight = float(input('Твой вес в кг (например, 75.5): '))
# Запрашиваем рост (в метрах) и сохраняем в user_height (тип float)
user_height = float(input('Твой рост в метрах (например, 1.75): '))

# 3. Логика расчетов
# Константы
WATER_PER_KG = 30   # 30 мл на 1 кг веса тела
ONE_LITER = 1000    # 1000 мл = 1 литр


# Формула ИМТ: вес разделить на (рост в квадрате)
def calc_bmi(user_weight, user_height):
    """Подсчет Индекса массы тела (ИМТ)"""
    # расчёт bmi (Индекс массы тела)
    bmi = (user_weight / (user_height ** 2))
    # округляем до 1 знака после запятой
    bmi = round(bmi, 1)
    return bmi


# Подсчет воды: вес * 30 мл
def calc_water_needed(user_weight):
    """Подсчет нормы воды в день в литрах"""
    # расчёт нормы воды в миллилитрах
    water_ml = user_weight * WATER_PER_KG
    # переводим в литры
    water_liters = (water_ml / ONE_LITER)
    # округляем до 1 знака после запятой
    water_needed = round(water_liters, 1)
    return water_needed


# 4. Вывод красивого результата
# Используем f-строки, чтобы вывести отчет
print('-' * 40)
print('*' * 40)
print('-' * 40)
# Выводим имя и возраст.
print(f'Отчет для пользователя: {user_name}, ({user_age} г.)')
# Выводим ИМТ (округленный до 1 знака) и норму воды.
print(f'Твой Индекс Массы Тела: {calc_bmi(user_weight, user_height)}')
print(f'Твоя норма воды: {calc_water_needed(user_weight)} л. в день')
print()
print('Расчёт окончен. Будьте здоровы!')
print('-' * 40)
# Конец
