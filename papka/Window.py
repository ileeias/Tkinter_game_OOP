from tkinter import *
from tkinter import messagebox
import random
import time


class Monster:
    def __init__(self, full_ehp: int, name: str, hp: int, mp: int, stats: dict):
        self.full_ehp = full_ehp
        self.name = name
        self.hp = hp
        self.mp = mp
        self.stats = stats

    def attack(self, target):
        import random
        canvas.delete(btn_eId)
        number = random.randint(0, 100)
        crit_chance = random.randint(0, 100)
        if number > target.stats['agility']:
            if crit_chance >= 50:
                target.hp = target.hp - self.stats['strength'] * 20
                print(self.name, 'critical hits', target.name, 'and hits', self.stats['strength'] * 20,
                      'critical damage!')
                message_enemy.set(
                    f'{self.name} Сильно бьёт по {target.name} \nи наносит ему {self.stats['strength'] * 20}')
                x = (200 * target.hp) // target.full_hp
                canvas.coords(hp_h, 60, 150, 60 + x, 130)
            else:
                target.hp = target.hp - self.stats['strength'] * 10
                print(self.name, 'hits', target.name, 'and hits', self.stats['strength'] * 10, 'damage!')
                message_enemy.set(f'{self.name} бьёт по {target.name} \nи наносит ему {self.stats['strength'] * 10}')
                x = (200 * target.hp) // target.full_hp
                canvas.coords(hp_h, 60, 150, 60 + x, 130)

        else:
            print(self.name, 'hits', target.name, 'and misses...')
            message_enemy.set(f'{self.name} промахивается \nпо {target.name}...')
        if target.hp <= 0:
            canvas.delete(hp_h)
            canvas.delete(btnId)
            canvas.delete(btnId2)
            canvas.delete(btnId3)
            message.set("Умер")
            message_enemy.set('Я Победил!')
            canvas.itemconfig(hero_image, state='hidden')
            return
        message.set('АЙ!')
class Spell:
    def __init__(self, name: str, mp: int, description: str, kind: str, value: int):
        self.name = name
        self.mp = mp
        self.description = description
        self.kind = kind
        self.value = value
class Hero:
    def __init__(self, full_hp: int, name: str, hp: int, mp: int, stats: dict, spells: list):
        self.full_hp = full_hp
        self.name = name
        self.hp = hp
        self.mp = mp
        self.stats = stats
        self.spells = spells

    def attack(self, target: Monster):
        global btn_eId
        import random
        number = random.randint(0, 100)
        crit_chance = random.randint(0, 100)
        if target == "None":
            print('игрок не нажал на кнопку "играть"')
            value = message.get()
            message.set('Нажми "ИГРАТЬ!"')
            return
        if number > target.stats['agility']:
            if crit_chance >= 50:
                target.hp = target.hp - self.stats['strength'] * 20
                print(self.name, 'critical hits', target.name, 'and hits', self.stats['strength'] * 20,
                      'critical damage!')
                message.set(f'{self.name} Сильно бьёт по {target.name} и наносит ему {self.stats['strength'] * 20}')
                message_enemy.set('Ой-Ё-Ё-й!')
                x = (200 * target.hp) // target.full_ehp
                canvas.coords(hp_e, 600, 150, 600 + x, 130)

            else:
                target.hp = target.hp - self.stats['strength'] * 10
                print(self.name, 'hits', target.name, 'and hits', self.stats['strength'] * 10, 'damage!')
                message.set(f'{self.name} бьёт по {target.name} \nи наносит ему {self.stats['strength'] * 10}')
                message_enemy.set('АЙ!')
                x = (200 * target.hp) // target.full_ehp
                canvas.coords(hp_e, 600, 150, 600 + x, 130)
        else:

            print(self.name, 'hits', target.name, 'and misses...')
            value = message.get()
            message.set(f'{self.name} промахивается по {target.name}...')
            message_enemy.set('Мозила!')
        btn_e = Button(text='Ход монста', command=lambda: target.attack(allmight))
        btn_eId = canvas.create_window(400, 250, anchor=NW, window=btn_e)

    def cast(self, target, spell: Spell):
        if target == "None":
            print('игрок не нажал на кнопку "играть"')
            value = message.get()
            message.set('Нажми "ИГРАТЬ!"')
            return
        if spell.mp > self.mp:
            print('Not enought mana! You have only', self.mp)
            message.set(f'Недостаточно манны!')
        else:
            if spell.kind == 'Damage':
                self.mp = self.mp - spell.mp
                target.hp = target.hp - spell.value
                print(self.name, 'casts', spell.name, 'and deals', target.name, spell.value, 'damage!')
                message.set(f'{self.name} Кастует {spell.name} и {target.name} получает {spell.value} урона')
            elif spell.kind == 'Heal':
                self.mp = self.mp - spell.mp
                target.hp = target.hp + spell.value
                print(self.name, 'casts', spell.name, 'and heals', target.name, spell.value, 'hp!')
                message.set(f'{self.name} кастует {spell.name} и лечит {target.name} на {spell.value} HP!')

    def info_enemy(self, target: Monster):
        if target == "None":
            print('игрок не нажал на кнопку "играть"')
            value = message.get()
            message.set('Нажми "ИГРАТЬ!"')
            return
        message.set(f'У этого существа {target.hp} HP---{target.mp} MP---\n{target.stats}')
def on_closing():
    if messagebox.askokcancel('Выход из приложения', 'Хотите выйти из приложения?'):
        tk.destroy()
def enemy():
    global opponent_game, opponent_image, hp_h, hp_e, btn_eId, full_ehp, full_hp
    monsters = [ogr, vampire, troll]
    opponent = monsters[random.randint(0, len(monsters) - 1)]
    print('Ваш противник могучий ', opponent.name, '!', sep='')
    opponent_game = opponent
    if allmight.stats['speed'] >= opponent.stats['speed']:
        flag = 'Hero'
    else:
        # btn_e = Button(text='Монстр начинает!', command=lambda: opponent.attack(allmight))
        # btn_eId = canvas.create_window(400, 250, anchor=NW, window=btn_e)
        opponent.attack(allmight)
        # message.set('АЙ!')
        flag = 'Monster'
    if opponent.hp < 0:
        value = message.get()
        message.set('ПОБЕДА!')
        message_enemy.set(f'{opponent.name} Мертв')
        canvas.delete(btnId)
        canvas.delete(btnId2)
        canvas.delete(btnId3)
        canvas.itemconfig(opponent_image, state='hidden')
        return
    if opponent_image:
        canvas.itemconfig(opponent_image, state='hidden')
    if opponent.name == 'Ogr':
        opponent_image = canvas.create_image(500, 155, anchor=NW, image=ogr_png)
        canvas.create_rectangle(60, 150, 260, 130, fill='black', outline="#004D40")
        hp_h = canvas.create_rectangle(60, 150, 260, 130, fill='red', outline="#004D40")
        canvas.create_rectangle(600, 150, 800, 130, fill='black', outline="#004D40")
        hp_e = canvas.create_rectangle(600, 150, 600 + 200, 130, fill='red', outline="#004D40")
        message_enemy.set('Я съем тебя!')
    elif opponent.name == 'Troll':
        opponent_image = canvas.create_image(500, 165, anchor=NW, image=troll_png)
        canvas.create_rectangle(60, 150, 260, 130, fill='black', outline="#004D40")
        hp_h = canvas.create_rectangle(60, 150, 260, 130, fill='red', outline="#004D40")
        canvas.create_rectangle(600, 150, 800, 130, fill='black', outline="#004D40")
        hp_e = canvas.create_rectangle(600, 150, 600 + 200, 130, fill='red', outline="#004D40")
        message_enemy.set('Я обгладаю твои косточки!')
    else:
        opponent_image = canvas.create_image(500, 155, anchor=NW, image=vampire_png)
        canvas.create_rectangle(60, 150, 260, 130, fill='black', outline="#004D40")
        hp_h = canvas.create_rectangle(60, 150, 260, 130, fill='red', outline="#004D40")
        canvas.create_rectangle(600, 150, 800, 130, fill='black', outline="#004D40")
        hp_e = canvas.create_rectangle(600, 150, 600 + 200, 130, fill='red', outline="#004D40")
        message_enemy.set('Мне нужна твоя Кровь!')
    canvas.delete(checkId)
    while opponent.hp > 0:
        tk.update()
    else:
        canvas.delete(hp_e)
        # enemy()


fireball = Spell('fireball', 100, 'Mage cast a fireball! Awesome!', 'Damage', 100)
lightning = Spell('lightning', 150, 'Mage cast a lightning!', 'Damage', 150)
small_heal = Spell('small_heal', 50, 'Heals You!', 'Heal', 50)

allmight = Hero(500, 'Рыцарь', 500, 500, {'speed': 5, 'strength': 6, 'agility': 1, 'intelligence': 3, 'luck': 5}, [fireball])

ogr = Monster(450, 'Ogr', 450, 50, {'speed': 2, 'strength': 3, 'agility': 50, 'intelligence': 3, 'luck': 5})
vampire = Monster(500, 'Drakula', 500, 300, {'speed': 5, 'strength': 10, 'agility': 0, 'intelligence': 5, 'luck': 0})
troll = Monster(300, 'Troll', 300, 300, {'speed': 7, 'strength': 3, 'agility': 10, 'intelligence': 0, 'luck': 0})

tk = Tk()
tk.protocol('WM_DELETE_WINDOW', on_closing)
tk.title('Приложение')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=900, height=400, bd=0, highlightthickness=0)
canvas.pack()
message = StringVar(value='Начнём игру?')
text_window = Label(tk, textvariable=message, font=('Arial', 15))
text_window.place(anchor="nw", x=50, y=70)
message_enemy = StringVar(value='[________]')
text_window2 = Label(tk, textvariable=message_enemy, font=('Arial', 15))
text_window2.place(anchor="nw", x=600, y=70)
check = Button(tk, text="ИГРАТЬ!", command=lambda: enemy())
checkId = canvas.create_window(450, 304, anchor=NW, window=check)
# check.place(anchor="nw", x = 450, y = 304, width=80, height=25)
opponent_game = "None"
opponent_image = None
test = Button(tk, text="Тест")
testbutton = canvas.create_window(800, 304, width=100, anchor=NW, window=test)
btn = Button(tk, text="Атака", command=lambda: allmight.attack(opponent_game))
btnId = canvas.create_window(240, 304, anchor=NW, window=btn)
# btn.place(anchor="nw", x=240, y=304, width=80, height=25)
btn2 = Button(text="Заклинание", command=lambda: allmight.cast(opponent_game, fireball))
btnId2 = canvas.create_window(240, 332, anchor=NW, window=btn2)
# btn2.place(anchor="nw", x=240, y=332, width=80, height=25)
btn3 = Button(text="Осмотреть", command=lambda: allmight.info_enemy(opponent_game))
btnId3 = canvas.create_window(240, 360, anchor=NW, window=btn3)
# btn3.place(anchor="nw", x=240, y=360, width=80, height=25)
btn_eId = canvas.create_rectangle(10, 10, 10, 10, fill='red', outline="#004D40")

canvas.create_line(0, 300, 900, 300, width=10)
canvas.create_rectangle(0, 300, 900, 600, fill='grey')
hero_png = PhotoImage(file='Hero.png')
ogr_png = PhotoImage(file='Ogr.png')
troll_png = PhotoImage(file='Trol.png')
vampire_png = PhotoImage(file='Vampir.png')
hero_image = canvas.create_image(200, 155, anchor=NW, image=hero_png)

# размеры прямоугольника
# big_size = (60, 60, 150, 150)
# small_size = (60, 60, 100, 100)
# # обработчики событий
# def make_big(event): canvas.coords(id, big_size)
# def make_small(event): canvas.coords(id, small_size)
# id = canvas.create_rectangle(small_size, fill="red")
# # привязка событий к элементу с идентификатором id
# canvas.tag_bind(id, "<Enter>", make_big)
# canvas.tag_bind(id, "<Leave>", make_small)

tk.mainloop()
