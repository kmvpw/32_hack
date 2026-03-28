#Персонаж: class Person Класс, содержащий в себе следующие параметры:

#Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты. Параметры передаются через конструктор;
#метод, принимающий на вход список вещей set_things(things);
#метод вычитания жизни на основе входной атаки, а также методы для выполнения алгоритма, представленного ниже;

class Person():
    def __init__(self, name, hp, base_attack, base_armor):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_armor = base_armor
    
    def set_things(self, things):
        pass
    
    def