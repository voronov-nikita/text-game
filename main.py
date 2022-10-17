import random

game = True

eat = ["гриб", "картошка", "хлеб", "вода"]
weapon = ['Дубина', 'Меч', 'Арбалет', 'пистолет', ]

events = ["Вы нашли золото", "Вы встретили монстра", f"Вы нашли {random.choice(eat)}",
          f"Вы нашли {random.choice(weapon)}", ]


class Hero:
    def __init__(self):
        self.life = 5
        self.dm = 10
        self.inventary = []
        self.weapon = ''
        self.golod = 20
        self.lvl = 1
        self.gold = 0

    def add_inventary(self, object):
        w = input("Подобрать(1) или нет(2)?")
        if w == '1':
            self.inventary.append(str(object))

    def eating(self):
        for i in eat:
            if i in self.inventary:
                w = input("Что хотите сьесть? \n")
                if w in self.inventary:
                    del self.inventary[self.inventary.index(str(w))]
                    self.golod += 4
                    print("Очень вкусно!")
                else:
                    print("Такого у вас нет!")

    def die(self):
        if self.life == 0:
            print("Game Over")
        else:
            self.life -= 1


class Evil:
    def __init__(self):
        self.life = 2
        self.dm = 5
        self.weapon = random.choice(weapon)


class Treasure:
    def __init__(self):
        self.gold = 10

    def add_gold(self):
        pass


def fight():
    pass


hero = Hero()
evil = Evil()
s = Treasure()

while game:
    go = input("Идти(1) или уйти(2)? \n")
    if go == '1':
        event = random.choice(events)
        print(event)
        if event == events[0]:
            hero.gold += 1
        elif event == events[1]:
            fight()
        elif event == events[2]:
            hero.add_inventary(event[2])
        elif event == events[3]:
            hero.weapon = event[2]
        print("--------------" * 100)
    else:
        print("Пока")
        break
