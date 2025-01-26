from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config import bot
from src.keyboard.keyboard import user_keyboard_button, keyboard_maker
from src.states.user_states import User

router2 = Router()


@router2.message(CommandStart())
async def user_role(message: Message, state:FSMContext):
    '''Задает вопрос выбора роли'''
    await bot.send_message(
        chat_id=message.chat.id,
        text="Здравствуйте, Вы родитель или ребенок?",
        reply_markup=keyboard_maker()
    )
    await state.set_state(User.wait_role)


@router2.message(F.text == user_keyboard_button["button 2"], User.wait_role)
async def request_age(message: Message, state:FSMContext):
    '''Вопрос "сколько лет человеку" '''
    await bot.send_message(
        chat_id=message.chat.id,
        text="Введите кол-во лет Вашего ребенка"
    )
    print("Пользователь - родитель")
    await state.set_state(User.wait_age)

@router2.message(User.wait_age)
async def enter_age(message: Message, state:FSMContext):
    if message.text.isdigit():
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"Возраст = {message.text}"
        )
        print(message.text)
        await state.set_state(User.wait_age)
    else:
        await bot.send_message(
            chat_id=message.chat.id,
            text="Ввозраст введен неверно"
        )
