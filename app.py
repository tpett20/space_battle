import random

# print(random.uniform(.6,.8))

alien_ships = ['Borg', 'Xxynzz', 'Bane', 'Taladune', 'f9-3000', 'Emperor Zillafar']
choice = "No"

class Player():
    def __init__(self, name):
        self.name = name
        self.hull = 20
        self.firepower = 5
        self.accuracy = .7
    
    def attacked(self, damage, success):
        if success: 
            self.hull -= damage
            print(f"{alien_ships[new_alien.ship_no-1]} hit you!")
        else: 
            print(f"{alien_ships[new_alien.ship_no-1]} missed you!")
    
    def accuracy_check(self):
        rand_num = random.uniform(0,1)
        if self.accuracy > rand_num:
            return True
        else: 
            return False

class Alien():
    ship_no = 0

    def __init__(self):
        self.id = Alien.ship_no
        Alien.ship_no += 1
        self.hull = random.uniform(3,6)
        self.firepower = random.uniform(2,4)
        self.accuracy = random.uniform(.6,.8)

    def attacked(self, damage, success):
        if success: 
            self.hull -= damage
            print("Direct hit!")
        else: 
            print("You missed!")
    
    def accuracy_check(self):
        rand_num = random.uniform(0,1)
        if self.accuracy > rand_num:
            return True
        else: 
            return False

name = input("Enter the name of your vessel: ")

player1 = Player(name)
print(f"Greetings, {player1.name}!\nAre you ready for battle?\nAre you ready for war?\n")

while player1.hull > 0 and Alien.ship_no < 6 and choice != "Yes":
    new_alien = Alien()
    print(f"\n\n\nAlien Ship #{new_alien.ship_no},  {alien_ships[new_alien.ship_no-1]} approaches\n\n\n -----------------------------------")
    while new_alien.hull > 0 and player1.hull > 0: 
        print(f"{player1.name}'s Hull: {round(player1.hull, 2)} | Alien Hull: {round(new_alien.hull,2)}")

        print(f"You're the first to attack!\n")
        new_alien.attacked(player1.firepower, player1.accuracy_check())
        print(f"\n-----------------------------------\nYour Hull: {round(player1.hull,2)}")
        print(f"{alien_ships[new_alien.ship_no-1]}'s Hull: {round(new_alien.hull,2)}")
        print(f"Brace Yourselves!")
        player1.attacked(new_alien.firepower, new_alien.accuracy_check())
        
    choice =  input("Give up on humanity? Yes or No ")
    


if choice == "Yes":
    print("Humanity is most dissappointed, coward...")
elif player1.hull > 0:
    print(f"\nYou win!! and with {player1.name} having {round(player1.hull,2)} life to spare")
else:
    print(f"\nYou died! Humanity is doomed")