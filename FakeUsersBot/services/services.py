import requests

users: dict[int, str] = {}
posts: dict[int, str] = {}
_user_names: dict[int, str] = {}


def get_users():
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    counter = 1
    for user in response.json():
        if user['id'] not in _user_names:
            _user_names[user['id']] = user['name']

        text = (f'<b>Имя:</b> {user["name"]}\n'
                f'<b>Username:</b> {user["username"]}\n'
                f'<b>Адрес:</b> {user["address"]["city"]}, {user["address"]["street"]}, {user["address"]["suite"]}\n'
                f'<b>Email:</b> {user["email"]}\n'
                f'<b>Номер телефона:</b> {user["phone"]}\n'
                f'<b>Место работы:</b> {user["company"]["name"]}\n'
                f'<b>ID пользователя:</b> {user["id"]}')
        users[counter] = text
        counter += 1


def get_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    counter = 1
    for post in response.json():
        user = _user_names[post['userId']]

        text = (f'{post["title"].title()}\n\n'
                f'{post["body"].title()}\n\n'
                f'<b>Автор:</b> {user}')
        posts[counter] = text
        counter += 1


def get_specific_user(user_id):
    url = f'https://jsonplaceholder.typicode.com/users?id={user_id}'
    response = requests.get(url)
    if response.json() == []:
        return 'Пользователь с таким ID мне не знаком'

    user = response.json()[0]

    text = (f'<b>Имя:</b> {user["name"]}\n'
            f'<b>Username:</b> {user["username"]}\n'
            f'<b>Адрес:</b> {user["address"]["city"]}, {user["address"]["street"]}, {user["address"]["suite"]}\n'
            f'<b>Email:</b> {user["email"]}\n'
            f'<b>Номер телефона:</b> {user["phone"]}\n'
            f'<b>Место работы:</b> {user["company"]["name"]}\n'
            f'<b>ID пользователя:</b> {user["id"]}')
    return text


def get_specific_posts(user_id):
    url = f'https://jsonplaceholder.typicode.com/posts?userId={user_id}'
    response = requests.get(url)
    specific_posts: dict[int, str] = {}
    counter = 1
    for post in response.json():
        user = _user_names[post['userId']]
        text = (f'{post["title"].title()}\n\n'
                f'{post["body"].title()}\n\n'
                f'<b>Автор:</b> {user}')
        specific_posts[counter] = text
        counter += 1

    return specific_posts


get_users()
get_posts()
