from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.height = self.get_height()
        self.weight = self.get_weight()
        self.abilities = self.get_abilities()
<<<<<<< HEAD
        self.hunger = 100 #uroven goloda (primer dali 20 edibnic edi to on 100-20=80, umenšil tekušij uroven goloda)
=======
>>>>>>> bfcb381bda48d0f74a75d96d835ab6f52c95c7d7

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        pass
    
    # Метод для получения имени покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "Pikachu"
    
    def get_height(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code ==200:
            data = response.json()
            return data['height']
        else:
            return "Unknown"

    def get_weight(self):
            url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data['weight']
            else:
                return "Unknown"
<<<<<<< HEAD
    
    def feed(self, food_amount):
        self.hunger = max(0, self.hunger - food_amount)#ctobi uroven goloda ne stanavilse niže urovna 0
        return f"{self.name} был накормлен на {food_amount} ед.!"

=======
>>>>>>> bfcb381bda48d0f74a75d96d835ab6f52c95c7d7

    def get_abilities(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            abilities = [ability['ability']['name'] for ability in data['abilities']]
            return abilities
        else:
            return "No abilities found"

    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return (f"Name: {self.name}\n"
                f"Height: {self.height}\n"
                f"Weight: {self.weight}\n"
                f"Abilities: {', '.join(self.abilities)}")

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img



