# Персонаж: class Person Класс, содержащий в себе следующие параметры:

# Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты. Параметры передаются через конструктор;
# метод, принимающий на вход список вещей set_things(things);
# метод вычитания жизни на основе входной атаки, а также методы для выполнения алгоритма, представленного ниже;

class Person:
    def __init__(self, name, base_health, base_attack, base_armor, things=None):
        self.name = name
        self.base_health = base_health
        self.base_attack = base_attack
        self.base_armor = base_armor

        self.additional_attack = 0
        self.additional_armor = 0
        self.additional_health = 0

        # По-сути костыль, но костыль со смыслом.
        # Мы в ходе игры не уменьшаем показатель здоровья,
        # а накапливаем повреждения
        self.damage_taken = 0

        # Одеваем персону в данную ему снарягу, если та подана при создании объекта.
        self.things = []
        if things:
            self.set_things(things)

    def set_things(self, things: list):
        # Даём Person-е список его вещей
        self.things += things

        for thing in things:
            self.additional_health += thing.health
            self.additional_attack += thing.attack
            self.additional_armor += thing.armor_percent

    def take_damage(self, enemy_attack_value):
        self.damage_taken += enemy_attack_value

    @property
    def health(self):
        return self.base_health + self.additional_health

    @property
    def armor(self):
        # Кап защиты 100%.
        return min(1, self.additional_armor + self.base_armor)

    @property
    def attack(self):
        return self.base_attack + self.additional_attack

    @property
    def current_health(self):
        return self.health - self.damage_taken


class Paladin(Person):
    def __init__(self, name, base_health, base_attack, base_armor, things=None):
        super().__init__(name, base_health, base_attack, base_armor, things=None)
        self.base_armor = 2 * self.base_armor
        self.base_health = 2 * self.base_health


class Warrior(Person):
    def __init__(self, name, base_health, base_attack, base_armor, things=None):
        super().__init__(name, base_health, base_attack, base_armor, things=None)
        self.base_attack = 2 * self.base_attack
