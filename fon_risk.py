import math


# Руководство по безопасности "Методические основы анализа опасностей и
# оценки риска аварий на опасных производственных объектах" от 03.11.2022 №387
# Таблица N 6-3

def risk_level(dead_people: int):
    if dead_people <= 5:
        return 'small'

    elif dead_people > 5 and dead_people <= 10:
        return 'medium'

    elif dead_people > 10 and dead_people <= 50:
        return 'high'

    elif dead_people > 50:
        return 'max'

    else:
        return 'max'


# Определение риска в ppm и dBR
def translation_values_risk(ind_risk: int):
    return (round(10 * math.log10(ind_risk * pow(10, 6) / Rgl), 2), ind_risk * pow(10, 6))


# Определение доп.мат. ущерба
def permissible_damage(damage: int, level_damage: int):
    if damage <= level_damage:
        return damage
    else:
        return level_damage * 0.8


# Приложение N 2
# к РБ "Методика установления допустимого
# риска аварии при обосновании безопасности опасных производственных
# объектов нефтегазового комплекса", утвержденному пр. Ростехнадзора от 12 сентября 2023 г. N 331
#
# Таблица N 1
data_background_risk_dead = {
    'Oil and gas': ('Нефтегазодобывающая промышленность', -4.3, 7.3),
    'Oil refining': ('Нефтеперерабатывающая промышленность', -5.8, 5.2),
    'Petrochemical': ('Нефтехимическая промышленност', -8.9, 2.3),
}

# Приложение N 2
# к РБ "Методика установления допустимого
# риска аварии при обосновании безопасности опасных производственных
# объектов нефтегазового комплекса", утвержденному пр. Ростехнадзора от 12 сентября 2023 г. N 331
#
# Таблица N 2
data_background_risk_damage = {
    'Oil and gas': ('Нефтегазодобывающая промышленность', 10, 97),
    'Oil refining': ('Нефтеперерабатывающая промышленность', 6, 409),
    'Petrochemical': ('Нефтехимическая промышленност', 6, 409),
}

# Приложение N 3
# к РБ "Методика установления допустимого
# риска аварии при обосновании безопасности опасных производственных
# объектов нефтегазового комплекса", утвержденному пр. Ростехнадзора от 12 сентября 2023 г. N 331
#
# Таблица N 4
reserve_ratio = {
    'small': 10,
    'medium': 20,
    'high': 50,
    'max': 100
}

reserve_ratio_Rgl = {
    'small': 100,
    'medium': 200,
    'high': 500,
    'max': 1000
}

# п. 14 РБ "Методика установления допустимого
# риска аварии при обосновании безопасности опасных производственных
# объектов нефтегазового комплекса", утвержденному пр. Ростехнадзора от 12 сентября 2023 г. N 331
reserve_ratio_cycle = {
    'project': 3,
    'present': 5,
    'population': 100
}

if __name__ == '__main__':
    print('Пример 1 Новое строительство на основе количества погибших')
    print('-' * 20)
    type_prom = 'Oil refining'
    cycle = 'project'
    cycle_population = 'population'
    dead_people = 8
    level = risk_level(dead_people)
    Rgl = 195  # ppm Таблица N 3 "Методика установления допустимого риска

    Rdb_personal = round(
        (data_background_risk_dead[type_prom][-1] * 10) / (reserve_ratio_cycle[cycle] * reserve_ratio[level]), 4)
    Rdb_population = round(((data_background_risk_dead[type_prom][-1] * 10) / (
            reserve_ratio_cycle[cycle] * reserve_ratio[level])) / reserve_ratio_cycle[cycle_population], 4)

    Rdb_personal_dBR = round(10 * math.log10(Rdb_personal / Rgl), 2)
    Rdb_population_dBR = round(10 * math.log10(Rdb_population / Rgl), 2)

    print(Rdb_personal, ' ppm (for personal')
    print(Rdb_population, ' ppm (for population)')
    print(Rdb_personal_dBR, ' dBR (for personal')
    print(Rdb_population_dBR, ' dBR (for population)')
    print('-' * 20)

    print('Пример 2 Сущ.объект на основе количества Rgl')
    dead_people = 8
    level = risk_level(dead_people)
    Rgl = 195  # ppm Таблица N 3 "Методика установления допустимого риска
    cycle = 'present'

    Rdb_personal = round((Rgl) / (reserve_ratio_cycle[cycle] * reserve_ratio_Rgl[level]), 4)
    Rdb_population = round(
        ((Rgl) / (reserve_ratio_cycle[cycle] * reserve_ratio_Rgl[level])) / reserve_ratio_cycle[cycle_population], 4)

    Rdb_personal_dBR = round(10 * math.log10(Rdb_personal / Rgl), 2)
    Rdb_population_dBR = round(10 * math.log10(Rdb_population / Rgl), 2)

    print(Rdb_personal, ' ppm (for personal')
    print(Rdb_population, ' ppm (for population)')
    print(Rdb_personal_dBR, ' dBR (for personal')
    print(Rdb_population_dBR, ' dBR (for population)')
    print('-' * 20)

    print('Пример мой Индивидуальный риск в ppm и dBR')
    print('-' * 20)
    ind_risk = 195 * pow(10, -6)
    print(translation_values_risk(ind_risk))
    print('-' * 20)

    print('Пример мой определение допустимого риска материального')
    print('-' * 20)
    damage = 200  # млн.
    type_prom = 'Oil refining'
    level_damage = data_background_risk_damage[type_prom][-1]
    risk_damage = permissible_damage(damage, data_background_risk_damage[type_prom][-1])
    print(risk_damage)
    print('-' * 20)
