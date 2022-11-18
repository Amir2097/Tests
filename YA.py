import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
API_TOKEN = "***"
headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {API_TOKEN}'}

def new_folder(path):
    '''Функция создает папку в Яндекс диске, а потом удаляет'''
    requests.put(URL, headers=headers, params={'path': path})
    del_res = requests.delete(URL, headers=headers, params={'path': path})
    return del_res.status_code
