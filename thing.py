class Thing():
    """
    Класс, представляющий игровую вещь.
    """
    def __init__(self, name, armor_percent, attack, health):
        self.name = name
        self.armor_percent = armor_percent
        self.attack = attack
        self.health = health

    def __str__(self):
        return f'Вещь: имя - {self.name}, броня - {self.armor_percent * 100}%, атака - {self.attack}, здоровье - {self.health}'