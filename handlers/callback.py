from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot


# @dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    # markup = InlineKeyboardMarkup()
    # button_1 = InlineKeyboardButton("efwefwfewf", callback_data="3")
    # markup.add(button_1)
    # await call.message.edit_reply_markup(markup)

    question = "В каком году был создан Python?"
    answers = [
        "1991",
        "2001",
        "1880",
        "2019",
        "2032",
        "3232",
    ]
    # await call.answer("")
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        open_period=10,
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_1")
