from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
from aiogram.utils.keyboard import (
ReplyKeyboardMarkup, ReplyKeyboardBuilder, InlineKeyboardBuilder, InlineKeyboardMarkup, KeyboardButton,
InlineKeyboardButton
)



start = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton("Функции"), KeyboardButton("О нас")]],
    resize_keyboard=True
)

functions = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton("Свое расписание"), KeyboardButton("Расписание звонков"), KeyboardButton("Расписание преподавателя")],
              [KeyboardButton("Фамилия преподавателя"), KeyboardButton("Числитель / Знаменатель")]],
    resize_keyboard=True
)

what_tt = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton("На сегодня"), KeyboardButton("На завтра"), KeyboardButton("На неделю")]],
    resize_keyboard=True
)

back = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton("Назад")]], resize_keyboard=True
)

confirm = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton("Да"), KeyboardButton("Нет")]], resize_keyboard=True
)