from config import dp, bot
from aiogram import types
import random



total = 0

@dp.message_handler(commands=['start', 'help'])
async def start_bot(message: types.Message):
    print(message)
    await message.reply(f'Привет, {message.from_user.first_name}!')
    print('Start')
    await message.answer("Я знаю такие команды: /help и  /start- справка по командам,  /candy игра в конфетки")


@dp.message_handler(commands='candy')
async def candy_start_bot(message: types.Message):
    global total
    total = 150
    print('конфетки начало')
    await message.reply(f'Привет, {message.from_user.first_name}! Давай сыграем в конфетки. На столе лежит {total} конфет. \n Можно брать от 1 до 28 за раз. Кто взял последнюю, тот и победил.')
    await candy_bot()




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
            if 0 < take < 29:
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
                await message.reply(f'{message.from_user.first_name}, не жульничай!')

    else:
        await message.reply(f'{message.from_user.first_name}, давай-ка цифрами')


@dp.message_handler()
async def all_bot(message: types.Message):
    print(message)
    print('All')
    await message.reply(f'{message.from_user.first_name}, давай лучше сыграем в конфетки! Пиши /candy')