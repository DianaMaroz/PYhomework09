from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b3 = KeyboardButton('/орел')
b4 = KeyboardButton('/решка')

kb_coin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_coin.add(b3).insert(b4)