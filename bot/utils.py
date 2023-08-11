"""Файл с состояниями."""

from aiogram.fsm.state import State, StatesGroup


class Route(StatesGroup):
    """Класс состояний для марштура."""
    route = State()
    exhibit = State()
    review = State()
    quiz = State()


class User(StatesGroup):
    """Класс состояний для пользователя."""
    age = State()
    name = State()
    hobby = State()
