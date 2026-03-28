from thing import Thing
import random
# Шаг 1 - создаем произвольное количество вещей с различными параметрами, процент защиты не должен превышать 10%(0.1). 
#    Сортируем по проценту защиты, по возрастанию;
MAX_TOTAL_THING = 100
MAX_ATTACK = 20
MAX_HEALTH = 20

total_thing = random.randint(1, MAX_TOTAL_THING)
names = ["sword", "helmet", "cloak", "magic_wand", "book_of_spells"]


things = [
    Thing(
        name=names[random.randint(0, len(names))],
        armor_percent=random.randint(0, 10),
        attack=random.randint(0, MAX_ATTACK),
        health=random.randint(0, MAX_HEALTH)
    )
    for _ in range(total_thing)
]



