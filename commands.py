from config import dp, bot
from aiogram import types
from keyboards import menu_key, coin_key
import random

total = 0


@dp.message_handler(commands=['start', 'help'])
async def start_bot(message: types.Message):
    print(message)
    await message.reply(f'Привет, {message.from_user.first_name}!')
    print('Start')
    await message.answer("Я знаю такие команды: /help и  /start- справка по командам,  /candy игра в конфетки")
    await message.reply('А вот и кнопочки!', reply_markup=menu_key.kb_menu)


@dp.message_handler(commands='candy')
async def candy_start_bot(message: types.Message):
    global total
    total = 150
    print('конфетки начало')
    await message.reply(f'Привет, {message.from_user.first_name}! Давай сыграем в конфетки. На столе лежит {total} конфет. \n Можно брать от 1 до 28 за раз. Кто взял последнюю, тот и победил.')
    await message.answer('Давай подбросим монетку. Выбирай: /орел или /решка? ', reply_markup=coin_key.kb_coin)
    #await candy_bot(message)

@dp.message_handler(commands= ['орел', 'решка'])
async def orel_reshka(message: types.Message):
    global total
    total = 150
    coin_random = random.choice(['орел', 'решка'])
    await message.answer(f'Сейчас подброшу монетку! {coin_random.capitalize()}!')
    if coin_random == 'орел':
        photo = open('pictures/ozel.jpg', 'rb')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
    else:
        photo = open('pictures/pagonya.jpg', 'rb')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
    if message.text[1:] == coin_random:
        await message.reply( f'Эй, {message.from_user.first_name}! Ты ходишь первым')
    else:
        await message.reply(f'Не повезло тебе, {message.from_user.first_name}! Первым хожу я')
        bot_take = random.randint(1, 28)
        total -= bot_take
        await message.answer(f'А я взял {bot_take} конфет и осталось {total}.')


@dp.message_handler()
async def candy_bot(message: types.Message):
    global total
    if message.text.isdigit():
        if total <= 0:
            await message.reply(f'{message.from_user.first_name}, '
                                f'а конфеток нет! Если хочешь, сыграть пиши /candy')
        else:
            take = int(message.text)
            print(f'{message.from_user.first_name} взял {take}')
            if take < 1 or take > 28 or take > total:
                await message.reply(f'{message.from_user.first_name}, не жульничай!')
            else:
                total -= take
                if total == 0:
                    await message.reply(f'{message.from_user.first_name}, '
                                    f'взял {take} конфет и осталось {total}.')
                    photo = open('pictures/hitriy-getsbi.jpg', 'rb')
                    await bot.send_photo(chat_id=message.chat.id, photo=photo)

                else:
                    await message.reply(f'{message.from_user.first_name}, '
                                        f'взял {take} конфет и осталось {total}')
                    bot_take = 0
                    if total < 29:
                        bot_take = total
                    else:
                        bot_take = random.randint(1, 28)
                    total -= bot_take
                    if total == 0:
                        await message.answer(f'А я взял {bot_take} конфет и осталось {total}.')
                        await message.answer('ЖАЛКИЙ КОЖАНЫЙ МЕШОК! Я ПОБЕДИЛ!')
                        photo = open('pictures/terminator.jpg', 'rb')
                        await bot.send_photo(chat_id=message.chat.id, photo=photo)
                    else:
                        await message.answer(f'А я взял {bot_take} конфет и осталось {total}')
    else:
        await message.reply(f'{message.from_user.first_name}, давай-ка цифрами')


@dp.message_handler()
async def all_bot(message: types.Message):
    print(message)
    print('All')
    await message.reply(f'{message.from_user.first_name}, давай лучше сыграем в конфетки! Пиши /candy')