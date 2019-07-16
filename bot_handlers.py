from bot import bot


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Привет, если у тебя есть ко мне вопрос, напиши его сюда, и я отвечу на него на "
                     "<a href='https://t.me/parislive61'>канале</a> в ближайшее время.\nВсе ответы публикуются "
                     "анонимно.\nТакже, прежде чем написать вопрос, проверь, нет ли на него уже ответа.",
                     parse_mode='HTML')
    bot.send_message("252048575", "С ботом начал общение: \n@" + message.from_user.username)


@bot.message_handler(commands=['channellink'])
def send_help(message):
    bot.send_message(message.chat.id, "https://t.me/parislive61")


@bot.message_handler(content_types=["text"])  # Любой текст
def answer_message(message):
    if message.text[:1] == "/":
        bot.send_message(message.chat.id, "Такой команды нет")

    else:
        bot.forward_message("252048575", message.chat.id, message.message_id)


@bot.message_handler(
    content_types=['sticker', 'user', 'chat', 'photo', 'audio', 'document', 'video', 'voice', 'contact', 'location',
                   'venue', 'file'])
def answer_sticker(message):
    bot.send_message(message.chat.id, "Пиши только текст")


if __name__ == '__main__':
    bot.polling(none_stop=True)
