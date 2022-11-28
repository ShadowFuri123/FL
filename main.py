import telebot
from config import token
import time

bot = telebot.TeleBot(token)

try:
    file = open('admin.text', 'r')
    file.close()
except:
    file = open('admin.text', 'w')
    file.close()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Отправьте сообщение и адрес для ответа на него')

@bot.message_handler(content_types=['text'])
def reply(message):
    if message.text != 'set_admin_id':
        with open('admin.text', 'r') as file:
            try:
                for admin in file:
                    bot.forward_message(admin, message.chat.id, message.message_id)
                bot.send_message(message.chat.id, 'Спасибо! Сообщение успешно отправлено')
            except:
                bot.send_message(message.chat.id, 'Извините, возникла ошибка. Скоро она будет обязательно исправлена!')
    if message.text == 'set_admin_id':
        with open('admin.text', 'w') as file:
            try:
                admins = []
                admins.append(str(message.chat.id))
                for i in admins:
                    file.write(f'{i}\n')
                bot.send_message(message.chat.id, 'Вы успешно добавлены')
            except:
                bot.send_message(message.chat.id, 'Возникла ошибка')


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=2)
            break
        except telebot.apihelper.ApiException as e:
            bot.stop_polling()
            time.sleep(5)