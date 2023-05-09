from aiogram import types, Dispatcher
from config import bot


# @dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    question = "В каком году был создан Python?"
    answers = [
        "1991",
        "2001",
        "1880",
        "2019",
        "2032",
        "3232",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        open_period=10,
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_1")
