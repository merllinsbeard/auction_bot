from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Клавиатура для главного меню администратора
start_buttons = [
    
[
    InlineKeyboardButton(text='Перейти в главное меню', callback_data='mainmenu')
],
[
    InlineKeyboardButton(text='Посмотреть статистику', callback_data='statistics')
]
    
]


main_menu = [

[
    InlineKeyboardButton(text='Запустить аукцион', callback_data='start_auction'),
    InlineKeyboardButton(text='Добавить канал', callback_data='add_channel')
],    
[
    InlineKeyboardButton(text='Посмотреть статистику', callback_data='statistics')
]    

]


STARTBUTTONS = InlineKeyboardMarkup(inline_keyboard=start_buttons)
MAINMENU = InlineKeyboardMarkup(inline_keyboard=main_menu)
