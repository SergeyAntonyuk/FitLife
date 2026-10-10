"""Проект FitLife - MVP версия 1.0.

Программа запрашивает имя, возраст, вес и рост пользователя.
Рассчитывает индекс массы тела (ИМТ) и рекомендуемую
суточную норму воды, после чего выводит отчет.
"""
# Константы
WATER_PER_KG = 30       # 30 мл на 1 кг веса тела
ONE_LITER = 1000        # 1000 мл = 1 литр
SEPARATOR_LENGTH = 40   # Количество символов в разделителях отчёта

# 1. Знакомство
print('Приветствую! Я твой фитнес-бот. Давай знакомиться?')
print('Введи свои данные ниже.')

user_name = input('Твое имя: ').title()

while True:
    try:
        user_age = int(input('Твой возраст (полных лет): '))
        break
    except ValueError:
        print('Ошибка! Введи только количество полных лет, например, 35.')
        continue


# 2. Сбор данных
user_weight = float(
    input('Твой вес в кг (например, 75.5): ').replace(',', '.')
)
user_height = float(
    input('Твой рост в метрах (например, 1.75): ').replace(',', '.')
)


# 3. Логика расчетов
def calc_bmi(user_weight, user_height):
    """Рассчитать индекс массы тела (ИМТ).

    Формула: вес в кг / рост в метрах в квадрате.

    Аргументы:
        user_weight: Вес пользователя в килограммах.
        user_height: Рост пользователя в метрах.

    Возвращает:
        Значение ИМТ, округленное до одного знака после запятой.
    """
    bmi = user_weight / (user_height ** 2)
    return round(bmi, 1)


def calc_water_needed(user_weight):
    """Рассчитать суточную норму воды в литрах.

    Расчет производится из нормы 30 мл на 1 кг массы тела.

    Аргументы:
        user_weight: Вес пользователя в килограммах.

    Возвращает:
        Норму воды в литрах, округленную до одного знака
        после запятой.
    """
    water_ml = user_weight * WATER_PER_KG
    water_liters = water_ml / ONE_LITER
    return round(water_liters, 1)


bmi = calc_bmi(user_weight, user_height)
water_needed = calc_water_needed(user_weight)


# 4. Вывод красивого результата
print('-' * SEPARATOR_LENGTH)
print('*' * SEPARATOR_LENGTH)
print('-' * SEPARATOR_LENGTH)
print(f'Отчет для пользователя: {user_name}, ({user_age} г.)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Твоя норма воды: {water_needed} л. в день')
print()
print('Расчёт окончен. Будьте здоровы!')
print('-' * SEPARATOR_LENGTH)
