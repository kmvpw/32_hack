#Персонаж: class Person Класс, содержащий в себе следующие параметры:

#Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты. Параметры передаются через конструктор;
#метод, принимающий на вход список вещей set_things(things);
#метод вычитания жизни на основе входной атаки, а также методы для выполнения алгоритма, представленного ниже;

class Person:
    def __init__(self, name, hp, base_attack, base_armor, things=None):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_armor = base_armor

        # Одеваем персону в данную ему снарягу, если та подана при создании объекта.
        self.things = []
        if things:
            self.set_things(things)

    def set_things(self, things: list):
        # Даём Person-е список его вещей
        self.things += things

        for thing in things:
            self.hp += thing.health
            self.base_attack += thing.attack
            # Условие капа брони. Показатель защиты не более 100%.
            self.base_armor = min(self.base_armor + thing.armor_percent, 1)


class Paladin(Person):
    def __init__(self):
        super().__init__()
        self.base_armor = self.base_armor = min(2 * self.base_armor, 1)
        self.hp = 2 * self.hp



class Warrior(Person):
    def __init__(self):
        super().__init__()
        self.base_attack = 2 * self.base_attack
