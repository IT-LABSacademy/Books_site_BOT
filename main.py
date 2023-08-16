import logging
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
from button import *
from config import API_TOKEN
from api import get_book
import config


logging.basicConfig(level=logging.INFO)



bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    data = user_create(message.from_user.id)
    markup = category_buttons()
    if data:
        await message.answer("Assalomu alaykum", reply_markup=markup)
    else:
        await message.answer("<b>Kerakli kategoriyani tanlang.</b>",  reply_markup=markup, parse_mode='HTML')
    





@dp.callback_query_handler(Text(startswith='category_'))
async def send_welcome(call: types.CallbackQuery):
    inx = call.data.index('_')
    id = call.data[inx+1:]
    markup = buttons_by_category_id(id)
    if markup["inline_keyboard"] != []:
        await call.message.answer("<b>Kerakli Kitobni tanlang.</b>",  reply_markup=markup, parse_mode='HTML')
    else:
        await call.answer("Tez orada")

@dp.callback_query_handler(Text(startswith='book_'))
async def send_welcome(call: types.CallbackQuery):
    inx = call.data.index('_')
    id = call.data[inx+1:]
    data = get_book(id)
    info = ''
    photo = ''
    if data:
        if data[0]['book_img']:
            photo = data[0]['book_img']
            info = f"Nomi: {data[0]['book_name']}"
        else:
            photo = open('img/defaulphoto.jpg', 'rb')
            info = f"Nomi: {data[0]['book_name']}"
        await call.message.answer_photo(photo, info)


    





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)