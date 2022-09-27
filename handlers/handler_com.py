from handlers.handler import Handler


class HandlerCommands(Handler):
    def __int__(self, bot):
        super().__init__(bot)

    def pressed_btn_start(self, message):
        self.bot.send_message(message.from_user.first_name)