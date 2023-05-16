from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from .keyboards import start_markup
from database.bot_db import sql_command_random


# @dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    # if message.text == "/help":
    await message.answer(f"Салалекум {message.from_user.full_name}",
                         reply_markup=start_markup)


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "By whom invented Python?"
    answers = [
        "Harry Potter",
        "Putin",
        "Guido Van Rossum",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
    ]
    # await message.answer_poll()
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        open_period=10,
        reply_markup=markup
    )


async def info_handler(message: types.Message):
    await message.answer("Сам разбирайся!")


async def get_user(message: types.Message):
    user: tuple = await sql_command_random()
    await message.answer_photo(
        user[-1],
        caption=f"{user[3]} {user[4]} "
                f"{user[5]} {user[6]}\n{user[2]}"
    )


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(get_user, commands=['get'])

