import json
import os
import time
from InquirerPy import inquirer


class Info:
    def __init__(self):
        self.character = None
        self.gener = None
        self.apresented = False
        self.money = 80
        self.equipped = "Nenhum"
        self.inventory = []

    def start(self):
        self.loadstorage()

        if not self.apresented:
            self.falar("...")
            self.falar(".....")
            self.falar("Quanto tempo...")
            self.falar("Já não lembro mais o seu nome, você não esta mais igual.")
            self.falar("Mas você tem uma jornada pela frente. Esqueça o seu nome.")
            self.selectch()
        else:
            print(f"\nBem-vindo de volta, {self.character}!")
            self.menu()

    def selectch(self):
        ch = Characters().characters
        names = [char["nome"] for char in ch.values()]

        self.character = inquirer.select(
            message="A partir de hoje seu nome é?..",
            choices=names
        ).execute()

        self.verifych()

    def verifych(self):
        choice = inquirer.select(
            message="O que deseja fazer?",
            choices=['Ver infos', 'Selecionar', 'Voltar']
        ).execute()

        if choice == 'Ver infos':
            char = Characters().characters[self.character]

            print(
                f"\n\n❤ Vida | {char['vida']}"
                f"\n🏹 Ataque | {char['ataque']}"
                f"\n💨 Gênero | {char['genero']}\n"
            )

            inquirer.select(
                message="",
                choices=['Voltar']
            ).execute()

            return self.verifych()

        elif choice == "Selecionar":
            self.gener = Characters().characters[self.character]["genero"]
            self.apresented = True
            self.savestorage()

            print("\n✔ Personagem seleccionado.")
            self.menu()

        else:
            return self.selectch()

    def menu(self):
        while True:
            choice = inquirer.select(
                message="Menu principal:",
                choices=["Ver status", "Sair"]
            ).execute()

            if choice == "Ver status":
                print(
                    f"\n👤 {self.character}"
                    f"\n💰 Money: {self.money}"
                    f"\n🎒 Inventory: {self.inventory}"
                    f"\n⚔ Equipado: {self.equipped}\n"
                )
                input("Enter para voltar...")

            else:
                self.savestorage()
                print("Jogo salvo. Saindo...")
                break

    def savestorage(self):
        os.makedirs("User", exist_ok=True)

        storage = {
            "person": self.character,
            "genero": self.gener,
            "inventory": self.inventory,
            "money": self.money,
            "apresented": self.apresented
        }

        with open(f"User/{self.character}.json", "w") as f:
            json.dump(storage, f, indent=4)

    def loadstorage(self):
        if not os.path.exists("User"):
            return

        for file in os.listdir("User"):
            if file.endswith(".json"):
                with open(f"User/{file}", "r") as f:
                    dados = json.load(f)

                self.character = dados.get("person")
                self.gener = dados.get("genero")
                self.inventory = dados.get("inventory", [])
                self.money = dados.get("money", 0)
                self.apresented = dados.get("apresented", False)
                return

    def falar(self, texto):
        print(texto)
        time.sleep(2)


class Characters:
    def __init__(self):
        self.characters = {
            "Hero": {"nome": "Hero", "genero": "Masculino", "vida": 100, "ataque": 12},
            "Warrior": {"nome": "Warrior", "genero": "Masculino", "vida": 130, "ataque": 18},
            "Knight": {"nome": "Knight", "genero": "Masculino", "vida": 150, "ataque": 15},
            "Assassin": {"nome": "Assassin", "genero": "Masculino", "vida": 85, "ataque": 25},
            "Mage": {"nome": "Mage", "genero": "Masculino", "vida": 80, "ataque": 28},
            "Heroine": {"nome": "Heroine", "genero": "Feminino", "vida": 100, "ataque": 12},
            "Archer": {"nome": "Archer", "genero": "Feminino", "vida": 90, "ataque": 20},
            "Witch": {"nome": "Witch", "genero": "Feminino", "vida": 85, "ataque": 27},
            "Paladin": {"nome": "Paladin", "genero": "Feminino", "vida": 140, "ataque": 16},
            "Ninja": {"nome": "Ninja", "genero": "Feminino", "vida": 90, "ataque": 24}
        }


Info().start()