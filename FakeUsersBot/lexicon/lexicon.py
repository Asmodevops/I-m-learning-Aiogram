LEXICON: dict[str, str] = {
    'users_forward': '>>',
    'users_backward': '<<',
    'posts_forward': '>>',
    'posts_backward': '<<',
    'specific_posts_forward': '>>',
    'specific_posts_backward': '<<',
    '/start': 'Привет! Я бот, созданный для взаимодействия с <b>JSONPlaceholder</b>.\n'
              'Я могу помочь вам получить данные о пользователях и постах, оставленных данными пользователями.\n'
              'Чтобы узнать, что я умею, воспользуйтесь командой <b>/help</b>.',

    '/help': 'Вот список команд, которые я могу выполнить:\n\n'
             '<b>/ start</b> - Начало работы с ботом\n'
             '<b>/ help</b> - Показать это сообщение\n'
             '<b>/ users</b> - Получить список всех пользователей\n'
             '<b>/ user &lt;id&gt;</b> - Получить информацию о конкретном пользователе\n'
             '<b>/ posts</b> - Получить список всех постов\n'
             '<b>/ posts &lt;user_id&gt;</b> - Получить список всех постов конкретного пользователя\n'
             'Просто введите команду, и я предоставлю вам нужную информацию!',

    'get_users': 'Получить список пользователей',
    'get_posts': 'Получить список постов',
}

LEXICON_COMMANDS: dict[str, str] = {
    '/users': 'Получить список всех пользователей',
    '/posts': 'Получить список всех постов',
    '/help': 'Справка по работе бота'
}