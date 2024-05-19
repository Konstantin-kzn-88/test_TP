import random

data = {'Испытание КП': 2,
        'Удельное количество пересечений': 2,
        'Кол-во подземных переходов': 2,
        'Идентификация': 2,
        'Частота патрулирования': 2,
        'Коррозионность продукта': 2,
        'Состояние охранной зоны трубопровода': 2,

        'Внутренняя коррозия и эрозия': 3,
        'Регионы': 3,
        'Плотность населения': 3,
        'Эксплуатационная документация': 3,
        'Внутренние динамические нагрузки': 3,
        'Качетсво производства труб': 3,
        'Оценка риска': 3,
        'КРН': 3,

        'Превентивные мероприятия': 4,
        'Тисп': 4,
        'Время с момента последнего испытания': 4,
        'Коррозия под напряжением': 4,
        'Удаленность КП': 4,

        'Результат шурфования': 5,
        'Природные воздействия': 5,
        'Обоснование взрывоустойчивости зданий': 5,

        'Отн. Испытатеьного давления к рабочему': 6,
        'Планирование и организация работ': 6,
        'Внутренняя коррозия': 6,
        'Уровень антропогенной активности': 6,
        'Подвижки и деформация грунта': 6,

        'Качество СМР': 7,
        'Возможные мех. Воздействия': 7,
        'Уровень технической эксплуатации': 7,

        'Наружная коррозия': 9,
        'Наличие водотоков': 10,
        'ЛЭС': 10,
        'Температура продукта': 50
        }

true_ = 0
false_ = 0
data_list = list(data.keys())
random.shuffle(data_list)

for item in data_list:
    question = int(input(f'{item}-? ___'))
    if data[item] == question:
        print('Верно! =)')
        true_ += 1
    else:
        print('Не верно! =(')
        false_ += 1
    print('-' * 20)

print(true_, false_)

if __name__ == '__main__':
    ...
