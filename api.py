import config
import requests

url = config.MYURL


headers = {
    'Authorization': f'token {config.MYTOKEN}'
}


def get_category():
    http = f"{url}category_all/"
    r = requests.get(http, headers=headers)
    return r.json()


def get_by_category_id(id):
    http = f"{url}by_category_id/{id}/"
    r = requests.get(http, headers=headers)

    if r.status_code == 200:
        return r.json()
    else:
        return []


def get_book(id):
    http = f"{url}book_id/{id}/"
    r = requests.get(http, headers=headers)
    return r.json()


def user_create(telegram_id):
    http = f"{url}user_create/"
    r = requests.post(http, data={
        "telegram_id": telegram_id
        
    }, headers=headers)
    if r.status_code == 201:
        return True
    else:
        return False
    
