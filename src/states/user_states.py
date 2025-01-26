from aiogram.fsm.state import State, StatesGroup


class User(StatesGroup):
    wait_role = State()
    wait_age = State()
    wait_question = State()