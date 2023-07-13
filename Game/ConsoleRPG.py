import random

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.level = 1
        self.exp = 0

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage > 0:
            enemy.health -= damage
        else:
            damage = 0
        print(f"{self.name} attacks {enemy.name} and deals {damage} damage.")

    def level_up(self):
        self.level += 1
        self.attack += 5
        self.defense += 2
        self.health = 100
        print(f"{self.name} leveled up! Level: {self.level}")

    def gain_exp(self, exp):
        self.exp += exp
        if self.exp >= 10:
            self.level_up()
            self.exp = 0

    def is_alive(self):
        return self.health > 0

# Enemy class
class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_player(self, player):
        damage = self.attack - player.defense
        if damage > 0:
            player.health -= damage
        else:
            damage = 0
        print(f"{self.name} attacks {player.name} and deals {damage} damage.")

    def is_alive(self):
        return self.health > 0

# Create player and enemy instances
player = Player("Player")
enemy = Enemy("Enemy", 50, 8, 3)

# Game loop
game_over = False
while not game_over:
    print("\n" + "=" * 20)
    print("Player Stats:")
    print(f"Name: {player.name}")
    print(f"Level: {player.level}")
    print(f"Health: {player.health}")
    print(f"Attack: {player.attack}")
    print(f"Defense: {player.defense}")
    print(f"Experience: {player.exp}/10")
    print("=" * 20 + "\n")

    print("1. Attack")
    print("2. Run")
    choice = input("Enter your choice: ")

    if choice == "1":
        player.attack_enemy(enemy)
        if not enemy.is_alive():
            player.gain_exp(5)
            print(f"{enemy.name} defeated! You gained 5 experience points.")
            enemy = Enemy("Enemy", 50, 8, 3)
    elif choice == "2":
        print("You ran away!")
        enemy = Enemy("Enemy", 50, 8, 3)
    else:
        print("Invalid choice! Try again.")

    if not player.is_alive():
        print("Game over! You are defeated.")
        game_over = True

    if player.level == 5:
        print("Congratulations! You have reached the maximum level.")
        game_over = True