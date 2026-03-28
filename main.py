import random

from thing import Thing
from persons import Paladin, Warrior
# Шаг 1 - создаем произвольное количество вещей с различными параметрами, процент защиты не должен превышать 10%(0.1). 
#    Сортируем по проценту защиты, по возрастанию;
MAX_TOTAL_THING = 100
MAX_ATTACK_THING = 20
MAX_HEALTH_THING = 20
TOTAL_PERSONS = 10
MIN_BASE_HP_PERSON = 10
MIN_BASE_ATTACK = 1
MIN_BASE_ARMOR = 1
MAX_BASE_HP_PERSON = 100
MAX_BASE_ATTACK = 20
MAX_BASE_ARMOR = 20
MAX_THING_FOR_PERSON = 4
total_thing = random.randint(1, MAX_TOTAL_THING)
names = ["меч", "шлем", "плащ", "волшебная палочка", "книга заклинаний"]


things = [
    Thing(
        name=names[random.randint(0, len(names) - 1)],
        armor_percent=random.randint(0, 10),
        attack=random.randint(0, MAX_ATTACK_THING),
        health=random.randint(0, MAX_HEALTH_THING)
    )
    for _ in range(total_thing)
]
things.sort(key=lambda x: x.armor_percent, reverse=False)
for thing in things:
    print(thing)


#Шаг 2 - создаем произвольно 10 персонажей, кол-во воинов и паладинов произвольно. Имена персонажам тоже рандомные из созданного списка 20 имен.
#Придумайте своих уникальных персонажей или заставьте сражаться знаменитостей, посмотрим кто сильнее =)
person_last_names = [
    "ДиКаприо",
    "Хэнкс", 
    "Де Ниро",
    "Пачино",
    "Вашингтон",
    "Круз",
    "Питт",
    "Клуни",
    "Деймон",
    "Бэйл",
    "Дауни",
    "Джекман",
    "Смит",
    "Нортон",
    "Макконахи",
    "Гослинг",
    "Дикинсон",
    "Стрейзанд",
    "Робертс",
    "Джоли"
]

total_paladins = random.randint(0, TOTAL_PERSONS)
total_warriors = TOTAL_PERSONS - total_paladins
persons = set()
for _ in range(total_paladins):
    persons.add(Paladin(
        name=person_last_names[random.randint(0, len(person_last_names) - 1)],
        base_health=random.randint(MIN_BASE_HP_PERSON, MAX_BASE_HP_PERSON),
        base_attack=random.randint(MIN_BASE_ATTACK, MAX_BASE_ATTACK),
        base_armor=random.randint(MIN_BASE_ARMOR, MAX_BASE_ARMOR)
    ))
for _ in range(total_paladins):
    persons.add(Warrior(
        name=person_last_names[
            random.randint(0, len(person_last_names) - 1)
        ],
        base_health=random.randint(
            MIN_BASE_HP_PERSON, MAX_BASE_HP_PERSON
        ),
        base_attack=random.randint(
            MIN_BASE_ATTACK, MAX_BASE_ATTACK
        ),
        base_armor=random.randint(
            MIN_BASE_ARMOR, MAX_BASE_ARMOR
        )
    ))
#for person in persons:
 #   print(person)
#Шаг 3 - одеваем персонажей рандомными вещами. Кому-то 1, кому-то больше, но не более 4 вещей в одни руки;
for person in persons:
    things_person =[things[random.randint(0, len(things) - 1)] for _ in range(random.randint(1, MAX_THING_FOR_PERSON))]
    person.set_things(things_person)
for person in persons:
    print(person)