import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token)

feeding_states = {}

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.img)
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['feed'])
def feed_pokemon_start(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        feeding_states[message.from_user.username] = True #пользователь находится в процессе кормления
        bot.send_message(message.chat.id, "Сколько еды ты хочешь дать своему покемону?")
    else:
        bot.reply_to(message, "Сначала создай покемона с помощью команды /go")

@bot.message_handler(func=lambda message: message.from_user.username in feeding_states)
def process_feed_amount(message):
    try:
        food_amount = int(message.text)
        pokemon = Pokemon.pokemons[message.from_user.username]
        response = pokemon.feed(food_amount)
        bot.send_message(message.chat.id, response)
        del feeding_states[message.from_user.username]  # Убираем пользователя из состояния кормления
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введи корректное число.")

bot.infinity_polling(none_stop=True)
