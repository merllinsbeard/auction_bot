from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ORM.models import Channel

main_menu = [
    
[
    InlineKeyboardButton(text='Запустить аукцион', callback_data='START_AUCTION'),
    InlineKeyboardButton(text='Добавленные каналы', callback_data='ADDED_CHANNELS')
],

[
    InlineKeyboardButton(text='Статистика по каналам', callback_data='STATISTICS'),
]

]

added_channels_back = [

[
    InlineKeyboardButton(text='Назад', callback_data='back_to_main_from_added_channels'),
]    

]

start_over = [
    [InlineKeyboardButton(text='Начать сначала', callback_data='start_over')]
]


start_or_no = [
    [InlineKeyboardButton(text='Начать сначала', callback_data='start_over')],
    [InlineKeyboardButton(text='Подтвердить', callback_data='confirm')]
]

async def generate_channel_keyboard(page=0):
    len_of_page = 5
    offset = page * len_of_page
    channels = await Channel.all().offset(offset).limit(len_of_page + 1).values('channel_id', 'channel_name')
    
    keyboard_buttons = []
    for channel in channels[:len_of_page]:
        button_text = channel['channel_name']
        button_callback = f"channel_{channel['channel_id']}"
        keyboard_buttons.append([InlineKeyboardButton(text=button_text, callback_data=button_callback)])
    
    navigation_buttons = []
    if page > 0:
        navigation_buttons.append(InlineKeyboardButton(text="⬅️ Назад", callback_data=f"page_{page - 1}"))
    if len(channels) > len_of_page:
        navigation_buttons.append(InlineKeyboardButton(text="Вперед ➡️", callback_data=f"page_{page + 1}"))
    
    # Добавление кнопок навигации
    if navigation_buttons:
        keyboard_buttons.append(navigation_buttons)

    # Добавление кнопки "Главное меню" в отдельной строке
    keyboard_buttons.append([InlineKeyboardButton(text="Главное меню", callback_data="go_to_main_menu_from_added_channels")])

    # Инициализация InlineKeyboardMarkup с наполненным списком кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)

    return keyboard

START_OR_NO = InlineKeyboardMarkup(inline_keyboard=start_or_no)
START_OVER = InlineKeyboardMarkup(inline_keyboard=start_over)
MAIN_MENU = InlineKeyboardMarkup(inline_keyboard=main_menu)
ADDED_CHANNELS_BACK = InlineKeyboardMarkup(inline_keyboard=added_channels_back)

