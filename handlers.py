from aiogram import types, Dispatcher

import commands


def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start_bot, commands=['start', 'help'])
    dp.register_message_handler(commands.candy_start_bot, commands='candy')
    dp.register_message_handler(commands.orel_reshka, commands=['орел', 'решка'])
    dp.register_message_handler(commands.candy_bot)
    dp.register_message_handler(commands.all_bot)

