import telebot
import re
from config import TOKEN, CHAT_ID, REGEXP


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(regexp=REGEXP)
def remove_message(message):
    bot.delete_message(chat_id=CHAT_ID,
                       message_id=message.message_id)


if __name__ == '__main__':
    bot.polling(none_stop=True,
                interval=0)
