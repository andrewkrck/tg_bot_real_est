"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from os import listdir, path
from random import choice
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from environs import Env

environ = Env()
if environ.bool("READ_ENV", True):
    environ.read_env()

API_TOKEN = environ.str("API_TOKEN", "BOT TOKEN HERE")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


class Form(StatesGroup):
    city = State()
    property_type = State()
    operation = State()


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(regexp="^search$")
async def search_property(message: types.Message):
    await Form.city.set()
    await message.reply("Де?")


@dp.message_handler(state=Form.city)
async def process_name(message: types.Message, state: FSMContext):
    """
    Process user name
    """
    async with state.proxy() as data:
        data['name'] = message.text

    await message.reply(f"How old are you? {state.proxy()}")

    await Form.next()
    await message.reply("How old are you?")


@dp.message_handler(regexp="^frog$")
async def frogs(message: types.Message):
    frog_name = choice(listdir("frogs"))
    frog_path = path.join("frogs", frog_name)
    with open(frog_path, "rb") as photo:
        """
        # Old fashioned way:
        await bot.send_photo(
            message.chat.id,
            photo,
            caption='Cats are here 😺',
            reply_to_message_id=message.message_id,
        )
        """

        await message.reply_photo(photo, caption="Frogs are here 🐸")


# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)

    # await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
