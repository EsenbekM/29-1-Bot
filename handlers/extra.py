from aiogram import types, Dispatcher
from config import bot
from asyncio import sleep


# DRY - Don't Repeat Yourself
# @dp.message_handler()
async def echo(message: types.Message):
    bad_words = ["js", "html", "дурак", "жинди"]
    username = f"@{message.from_user.username}" \
        if message.from_user.username else message.from_user.full_name
    for word in bad_words:
        if word in message.text.lower().replace(' ', ''):
            # await bot.delete_message(message.chat.id, message.message_id)
            await message.delete()
            await message.answer(
                f"Не матерись {username}, сам ты {word}!"
            )

    if message.text.startswith('.'):
        # await bot.pin_chat_message(message.chat.id, message.message_id)
        await message.pin()

    if message.text == "dice":
        a = await bot.send_dice(message.chat.id, emoji="🎲")
        await sleep(3)
        await message.answer("2113131")
        # print(a.dice.value)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
