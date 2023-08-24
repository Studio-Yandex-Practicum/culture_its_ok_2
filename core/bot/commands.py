"""Основные команды бота. Кнопки старт и маршруты"""
from aiogram import Bot, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from . import message as ms
from .config import ADMIN_ID
from .handlers import meetings_router, route_router
from .keyboards import set_command
from .utils import User

main_router = Router()
main_router.include_router(meetings_router)
main_router.include_router(route_router)


@main_router.startup()
async def start_bot(bot: Bot) -> None:
    await set_command(bot)
    await bot.send_message(ADMIN_ID, "Бот начал свою работу")


@main_router.shutdown()
async def end_bot(bot: Bot) -> None:
    await bot.send_message(ADMIN_ID, "Бот перестал работать")


@main_router.message(Command("help"))
async def help_info(message: Message) -> None:
    commands = {
        "/start": "Нажмите для приветсвеного сообщения",
        "/routes": "Нажмите для выбора маршрута",
        "/cancel": "Нажмите для отмены команды",
        "/help": "Нажмите для просмотра доступных команд"
    }
    text = ''
    for command in commands:
        text += f'{command}\n {commands[command]} \n'
    await message.reply(text)


@main_router.message(Command("cancel"))
@main_router.message(F.text.casefold() == "отмена")
async def cmd_cancel(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=ReplyKeyboardRemove()
    )


@main_router.message(CommandStart())
async def command_main_start(message: Message, state: FSMContext) -> None:
    """Команда /start. Должна приветствовать пользователя."""
    await message.answer(
        text=ms.GREETING_MESSAGE,
    )
    await message.answer("Давай познакомимся.\nКак тебя зовут?")
    await state.set_state(User.name)
