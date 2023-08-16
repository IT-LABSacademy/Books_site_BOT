from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup
from api import *


menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Categtories")
        ],
         [
            KeyboardButton("Books")
        ]
    ], resize_keyboard=True
)

def category_buttons():
    data = get_category()
    button = InlineKeyboardMarkup(row_width=2)
    for i in data:
       button.insert(InlineKeyboardButton(text=i['name'], callback_data=f"category_{i['id']}"))
    return button


def buttons_by_category_id(id):
    data = get_by_category_id(id)
    button = InlineKeyboardMarkup(row_width=2)
    if data != []:
        for i in data:
            button.insert(InlineKeyboardButton(text=i['book_name'], callback_data=f"book_{i['id']}"))
        return button
    else:
        return button


btn = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Telefon raqam yuborish" , request_contact=True)
        ]
    ], resize_keyboard=True
)

