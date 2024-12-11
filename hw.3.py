from main import Hero

class Uchihas(Hero):
    def unique_attack(self):
        print(f"{self.name} делает уникальную атаку!")

    def unique_scream(self):
        print(f"{self.name} издает уникальный крик!")

    def action(self):
        random_action = self.get_random_action()
        if random_action == 1:
            self.attack()
        elif random_action == 2:
            self.protection()
        elif random_action == 3:
            self.rest()


joker = Uchihas("Joker", 1000, 50)


joker.action()
joker.unique_scream()
joker.unique_attack()
joker.protection()
joker.attack()


