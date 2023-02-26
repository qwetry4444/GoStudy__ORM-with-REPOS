from aiogram import types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Dispatcher as dp
from misc.throttling import rate_limit
from aiogram.utils.i18n import gettext as _
from bot.states import States
# import bot.keyboards
import messages
from db.functions.user_func import user_exist, create_user, get_user
from sqlalchemy.orm import sessionmaker


# @rate_limit
async def start(message: types.Message, db) -> Message:
    if await user_exist(user_tg_id=message.from_user.id, db=db):
        print('Ye)')
    else:
        print("nope(")
    return await message.answer('))')

    # if db.user_exists(message.from_user.id):
    #     await message.answer(messages.WELCOME_MESSAGE, reply_markup=keyboards.start)
    # else:
    #     await message.answer(messages.WELCOME_MESSAGE)
    #     await message.answer(messages.REGISTRATION_MESSAGE)
    #     States.Registration.set()

# @rate_limit
# @dp.message_handler(state=States.Registration)
# async def registration(message: types.Message, state: FSMContext):
#     group_number = message.text
#     while True:
#
#         if message.text in messages.groups:
#             db.add_user(0, message.from_user.id, message.from_user.full_name, group_number)
#             await message.answer(messages.end_registration, reply_markup=keyboards.start)
#             break
#         else:
#             await message.answer(messages.group_number_fall)
#
#     await state.update_data(answer1=group_number)
#
#     await state.finish()
#
#
# @rate_limit
# @dp.message_handler(Text("О нас"))
# async def about_us(message: types.Message):
#     await message.answer(messages.ABOUT_US_MESSAGE)
#
#
# @rate_limit
# @dp.message_handler(Text("Функции"))
# async def functions(message: types.Message):
#     await message.answer(messages.FUNCTION_MESSAGE, reply_markup=keyboards.functions)
#
#
# @rate_limit
# @dp.message_handler(Text("Свое расписание"), state=None)
# async def student_tt(message: types.Message):
#     await message.answer(messages.what_tt, reply_markup=keyboards.what_tt)
#     await States.Ques_What_tt.set()
#
#
# @rate_limit
# @dp.message_handler(state=States.Ques_What_tt)
# async def student_ques_what_tt(message: types.Message, state: FSMContext):
#     answer = message.text
#     group_number = await db.get_user_group(message.from_user.id)
#     await state.update_data(answer1=answer)
#
#     if answer == "На завтра":
#         await message.answer(messages.get_tt)
#         await message.answer(db.get_tt_tomorrow(group_number,
#                              switchWeekday(datetime.datetime.today().weekday() + 1)),
#                              reply_markup=keyboards.functions)
#
#     elif answer == "На сегодня":
#         await message.answer(messages.get_tt)
#         await message.answer(db.get_tt_today(group_number, switchWeekday(datetime.datetime.today().weekday())),
#                              reply_markup=keyboards.functions)
#
#     elif answer == "На неделю":
#         await message.answer(messages.get_tt)
#         await message.answer(db.get_tt_week(group_number),
#                              reply_markup=keyboards.functions)
#
#     await state.finish()
#
#
# @rate_limit
# @dp.message_handler(Text("Расписание звонков"))
# async def get_tt_calls(message: types.Message):
#     await message.answer(messages.TT_cals)
#     await message.answer(Time.tt_Time())
#
#
# @rate_limit
# @dp.message_handler(Text("Расписание преподавателя"), state=None)
# async def get_tt_Lec(message: types.Message):
#     await message.answer(messages.SELECT_NAME_LECTURER, reply_markup=keyboards.back)
#     await States.Get_Lecturer_tt.set()
#
#
# @rate_limit
# @dp.message_handler(Text("Числитель / Знаменатель"))
# async def get_tipe_weel(message: types.Message):
#     await message.answer(Time.get_ch_zn())
#
#
# @rate_limit
# @dp.message_handler(Text("Назад"))
# async def back(message: types.Message):
#     await message.answer(messages.FUNCTION_MESSAGE, reply_markup=keyboards.functions)
#
#
# @rate_limit
# @dp.message_handler(state=States.Confirm)
# async def confirm(message: types.Message, state: FSMContext):
#     if message.text == "Да":
#         with await state.proxy() as data:
#             db.change_user_group(message.from_user.id, data['group'])
#             await message.answer(create_message.change_group_successful(data['group']))
#         await state.finish()
#     else:
#         await message.answer("Окей, отменил", reply_markup=keyboards.functions)
#
#
# @rate_limit
# @dp.message_handler(Text, state=States.Get_Lecturer_tt)
# async def get_what_Lec_tt(message: types.Message, state: FSMContext):
#     if message.text.lower() not in messages.lecturers_lastnames:
#         await message.answer(messages.WRONG_SELECT_NAME_LEC)
#     else:
#         await message.answer(db.get_tt_lecther(message), reply_markup=keyboards.functions)
#         await state.finish()
#
#
# @rate_limit
# @dp.message_handler(Text, state=None)
# async def change_group_number(message: types.Message, state: FSMContext):
#     if message.text in messages.groups:
#
#         await States.Confirm().set()
#         async with state.proxy() as data:
#             data['group'] = message.text

# @dp.message_handler(state=None)
# async def another(message: types.Message, state: FSMContext):
