from aiogram.types import Message, CallbackQuery
from aiogram import Bot, Dispatcher, executor, types
from keyboards import *
import random

from main import *

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=greet_kb)

@dp.message_handler(commands=['hi1'])
async def process_hi1_command(message: types.Message):
    await message.reply("Первое - изменяем размер клавиатуры", reply_markup=greet_kb1)

@dp.message_handler(commands=['hi2'])
async def process_hi1_command(message: types.Message):
    await message.reply("Второе - изменяем размер клавиатуры", reply_markup=greet_kb2)

@dp.message_handler(commands=['hi3'])
async def process_hi3_command(message: types.Message):
    await message.reply("Третье - добавляем больше кнопок", reply_markup=markup3)

@dp.message_handler(commands=['hi4'])
async def process_hi4_command(message: types.Message):
    await message.reply("Четвертое - расставляем кнопки в ряд", reply_markup=markup4)

@dp.message_handler(commands=['hi5'])
async def process_hi5_command(message: types.Message):
    await message.reply("Пятое - добавляем ряды кнопок", reply_markup=markup5)

@dp.message_handler(commands=['hi6'])
async def process_hi5_command(message: types.Message):
    await message.reply("Шестое - запрашиваем контакт и геолокацию\n Эти две кнопки не зависят друг от друга", reply_markup=markup_request)

@dp.message_handler(commands=['hi7'])
async def process_hi7_command(message: types.Message):
    await message.reply("Седьмое - все методы вместе")


@dp.message_handler(commands=['1'])
async def process_command_1(message: types.Message):
    await message.reply("Первая инлайн кнопка", reply_markup=inline_kb1)

@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка')

@dp.callback_query_handler(lambda c: c.data and c.data.startwith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 2:
        await bot.answer_callback_query(callback_query.id, text = 'Нажата вторая кнопка')
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id, text = 'Нажата кнопка 5. \nА это текст может быть длиной до 200 символов', show_alert=True
        )
    else:
        await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f"Нажта инлайн кнопка! code={code}")

@dp.message_handler(commands=['2'])
async def process_command_2(message: types.Message):
    await message.reply("Отправляю все возможные кнопки", reply_markup=inline_kb_full)

