import pytest
from my_old_program import visits_in_russia, unique_ids, max_volume

geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']}]

ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}



def test_visits_in_russia():
    res = visits_in_russia(geo_logs)
    assert res == [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}]

def test_unique_ids():
    res = unique_ids(ids)
    assert res == [213, 15, 54, 119, 98, 35]


def test_max_volume():
    res = max_volume(stats)
    assert res == 'yandex'