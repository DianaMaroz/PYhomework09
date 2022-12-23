from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
b2 = KeyboardButton('/candy')

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu.row(b1, b2)