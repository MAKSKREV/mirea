





import asyncio


import logging

from aiogram.types import Dice, CallbackQuery


from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Dispatcher, Router, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, LabeledPrice,InputMediaPhoto
from aiogram.client.bot import Bot, DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import FSInputFile
from aiogram.fsm.state import StatesGroup, State

from aiogram.types.web_app_info import WebAppInfo
from aiogram.exceptions import TelegramBadRequest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fakulteti = [16, 14, 28, 15, 46, 13, 11, 47, 68, 45]
driver = webdriver.Chrome()
driver.get("https://priem.mirea.ru/accepted-entrants-list/")
import sqlite3
class AuthStates(StatesGroup):
    waiting_for_phone = State()
    waiting_for_code = State()
    waiting_for_password = State()

logging.basicConfig(level=logging.INFO)

bot = Bot(token="8360819683:AAHGFn0TfXM34gh41lVW5PpSvcj8mIEZN-I", default=DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = MemoryStorage()
router = Router()
dp = Dispatcher(storage=storage)
dp.include_router(router)



@router.message(Command("start"))  
async def cmd_start(message: types.Message):
    
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".chakra-text.css-ty7r4z"))
    )
    

    faculties = driver.find_elements(By.CSS_SELECTOR, ".chakra-text.css-ty7r4z")
    balls = driver.find_elements(By.CSS_SELECTOR, ".chakra-text.css-5gfn3t")
    

    for i, (faculty, ball) in enumerate(zip(faculties, balls), 1):
        if i in fakulteti:
            await message.answer(f"{i}. {faculty.text} | Балл: {ball.text}")




async def main():



    try:
        await dp.start_polling(bot)
    except (KeyboardInterrupt, asyncio.CancelledError):
        logging.info("Бот остановлен пользователем.")
    finally:

        await bot.session.close()

    




if __name__ == '__main__':
    asyncio.run(main())

