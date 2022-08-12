from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from db import add_users, del_users, show_users

ID = 1734006490


class Admin(StatesGroup):
    id_add = State()
    id_del = State()


async def start_add(message: types.Message):
    if message.from_user.id == ID:
        await Admin.id_add.set()
        await message.reply("Укажите id")


async def add_id(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['id'] = message.text

        async with state.proxy() as data:
            if add_users(str(data['id'])):
                await message.reply("Добавлено")
            else:
                await message.reply("Уже в базе")
        await state.finish()


async def start_del(message: types.Message):
    if message.from_user.id == ID:
        await Admin.id_del.set()
        await message.reply("Укажите id")


async def del_id(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['id'] = message.text

        async with state.proxy() as data:
            del_users(str(data['id']))
            await message.reply("Удалено")
        await state.finish()


async def users(message: types.Message):
    await message.reply(f"{'::'.join(show_users())}")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(start_add, commands=['Добавить'], state=None)
    dp.register_message_handler(add_id, state=Admin.id_add)
    dp.register_message_handler(start_del, commands=['Удалить'], state=None)
    dp.register_message_handler(del_id, state=Admin.id_del)
    dp.register_message_handler(users, commands=['Рассылка'], state=None)
