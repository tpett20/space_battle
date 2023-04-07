import random

# print(random.uniform(.6,.8))

class Player():
    def __init__(self, name):
        self.name = name
        self.hull = 20
        self.firepower = 5
        self.accuracy = .7
    
    def attacked(self, damage, success):
        if success: 
            self.hull -= damage
            print("Alien hit you!")
        else: 
            print("Alien missed you!")
    
    def accuracy_check(self):
        rand_num = random.uniform(0,1)
        if self.accuracy > rand_num:
            print('hello')
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
            print('hello')
            return True
        else: 
            return False

player1 = Player('USS Assembly')
print(f"Greetings, {player1.name}!\nAre you ready for battle?\nAre you ready for war?\n")

while player1.hull > 0 and Alien.ship_no < 6:
    new_alien = Alien()
    print(f"Alien #{new_alien.ship_no} approaches")
    while new_alien.hull > 0 and player1.hull > 0: 
        print(f"Your Hull: {player1.hull}")
        print(f"Alien Hull: {new_alien.hull}")
        print(f"You're the first to attack!")
        new_alien.attacked(player1.firepower, player1.accuracy_check())
        print(f"Your Hull: {player1.hull}")
        print(f"Alien Hull: {new_alien.hull}")
        player1.attacked(new_alien.firepower, new_alien.accuracy_check())