from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

user_keyboard_button = {
       "button 1": "Ребенок",
       "button 2": "Родитель",
       "button 3": "Сколько тебе лет?",
       "button 4": "Чем занимаешься?",
       "button 5": "Нет вопросов"
       }

# def inline_keyboard_maker():
#     inline_keyboard_builder = InlineKeyboardBuilder()
#     button1 = InlineKeyboardButton(text=user_keyboard_button["button 1"], callback_data='hello')
#     button2 = InlineKeyboardButton(text=user_keyboard_button["button 2"], callback_data='hay')
#     inline_keyboard_builder.row(button1, button2)
#     return inline_keyboard_builder.as_markup(resize_keyboard=True)

def keyboard_maker():
    keyboard_builder = ReplyKeyboardBuilder()
    button1 = KeyboardButton(text=user_keyboard_button["button 1"])
    button2 = KeyboardButton(text=user_keyboard_button["button 2"])
    keyboard_builder.row(button1)
    keyboard_builder.row(button2)
    return keyboard_builder.as_markup(resize_keyboard=True)


def question_keyboard_maker():
    keyboard_builder = ReplyKeyboardBuilder()
    button1 = KeyboardButton(text=user_keyboard_button["button 2"])
    button2 = KeyboardButton(text=user_keyboard_button["button 4"])
    button3 = KeyboardButton(text=user_keyboard_button["button 5"])
    keyboard_builder.row(button1)
    keyboard_builder.row(button2)
    keyboard_builder.row(button3)
    return keyboard_builder.as_markup(resize_keyboard=True)