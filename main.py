from abc import ABC, abstractmethod
import random

class Hero(ABC):
    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self.__random_action = random.randint(1, 3)

    def attack(self):
        print(f'{self.name} атакует с силой {self.hp} hp')

    def protection(self):
        print(f'{self.name} защищается с уровнем защиты {self.lvl} lvl')

    def rest(self):
        print(f'{self.name} отдыхает и восстанавливает силы.')

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    def get_random_action(self):
        return self.__random_action
