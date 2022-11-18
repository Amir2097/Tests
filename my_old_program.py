
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def visits_in_russia(geo_logs):
    '''Фильтрация визитов только из России'''
    new_list = []
    for geo in geo_logs:
        for visit in geo.values():
            if 'Россия' == visit[1]:
                new_list.append(geo)
    return new_list



def unique_ids(ids):
    '''Фильтрация гео-ID из значений словаря ids, получаем уникальные'''
    list_unique = []

    for users_id in ids.values():
        users_id = set(users_id)
        for unique_id in users_id:
            if unique_id in list_unique:
                continue
            else:
                list_unique.append(unique_id)

    return list_unique



def max_volume(stats):
    '''Получение названия канала с максимальным объемом'''
    for service, stat in stats.items():
        if stat == max(stats.values()):
            return service

