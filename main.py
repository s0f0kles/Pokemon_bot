import telebot 
from config import token
from random import randint

from logic import Pokemon, Wizard, Fighter


bot = telebot.TeleBot(token)

feeding_states = {}

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def start(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "You have already created your own Pokemon")

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

@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "You can only fight with Pokemon")
    else:
            bot.send_message(message.chat.id, "To attack, you need to respond to messages from the person you want to attack.")

bot.infinity_polling(none_stop=True)

