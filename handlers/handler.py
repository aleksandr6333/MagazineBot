import abc
from markup.markup import Keyboards
from data_base.dbalchemy import DBManager


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot):
        self.bot = bot
        self.keyboards = keyboards()
        self.BD = DBManager()

    @abc.abstractmetod
    def handle(self):
        pass
