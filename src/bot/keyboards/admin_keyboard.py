from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


main_menu = [
    
[
    InlineKeyboardButton(text='Запустить аукцион', callback_data='START_AUCTION'),
    InlineKeyboardButton(text='Добавленные каналы', callback_data='ADDED_CHANNELS')
],

[
    InlineKeyboardButton(text='Статистика по каналам', callback_data='STATISTICS'),
]

]


MAIN_MENU = InlineKeyboardMarkup(inline_keyboard=main_menu)


