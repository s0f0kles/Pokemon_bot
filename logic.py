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
        self.hunger = 100 #uroven goloda (primer dali 20 edibnic edi to on 100-20=80, umenšil tekušij uroven goloda)
        self.hp = randint(10, 100)
        self.power = randint(10, 100)

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
    
    def feed(self, food_amount):
        self.hunger = max(0, self.hunger - food_amount)#ctobi uroven goloda ne stanavilse niže urovna 0
        return f"{self.name} был накормлен на {food_amount} ед.!"

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
                f"Abilities: {', '.join(self.abilities)}\n"
                f"Hp: {self.hp}\n"
                f"Power: {self.power}")

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,5)
            if chance == 1:
                return "Pokemon Wizard used a shield in battle"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

class Wizard(Pokemon):
   def info(self):
       return "Your Pokemon is a Wizard\n" + super().info()


class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nThe fighter used a super attack with force:{super_power} "
    
    def info(self):
       return "Your Pokemon is a Fighter\n" + super().info()
if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))