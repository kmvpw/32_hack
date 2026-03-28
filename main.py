from thing import Thing
import random
# Шаг 1 - создаем произвольное количество вещей с различными параметрами, процент защиты не должен превышать 10%(0.1). 
#    Сортируем по проценту защиты, по возрастанию;
total_thing = random.randint(1, 100)
names = ["sword", "helmet", "cloak", "magic_wand", "book_of_spells"]
MAX_ATTACK = 20

things = [
    Thing(
        name=names[random.randint(0, len(names))],
        armor_percent=random.randint(0, 10),
        attack=random.randint(0, MAX_ATTACK),
        health=)
    for _ in range(total_thing)
]



