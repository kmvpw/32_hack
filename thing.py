#Класс содержит в себе следующие параметры - название, процент защиты, атаку и жизнь
class Thing():
    def __init__(self, name, armor_percent, attack, health):
        self.name = name
        self.armor_percent = armor_percent
        self.attack = attack
        self.health = health
