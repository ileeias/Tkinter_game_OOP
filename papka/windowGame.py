from tkinter import *
from tkinter import messagebox
import time
def on_closing():
    if messagebox.askokcancel('Выход из приложения', 'Хотите выйти из приложения?'):
        tk.destroy()
def enemy():
    global opponent_image, hero_image, hp_h, hp_e, hp_h2, hp_e2, opponent_game, start_btn, yVelocity
    # while True:
    #     coord = canvas.coords(vampire_image)
    #     if coord[1] == 130 or coord[1] == 100:
    #         yVelocity = -yVelocity
    #     canvas.move(vampire_image, 0, yVelocity)
    #     tk.update()
    #     time.sleep(0.05)
    message.set('Начнём?')
    opponent = monsters[0]
    opponent_game = opponent
    if allmight.stats['speed'] >= opponent.stats['speed']:
        flag = 'Hero'
    else:
        opponent.attack(allmight)
        flag = 'Monster'

    if opponent.name == 'Ogr':
        opponent_image = ogr_image
        canvas.coords(ogr_image, 400, 155)
        hp_h2 = canvas.create_rectangle(170, 150, 370, 170, fill='black', outline="#004D40")
        hp_h = canvas.create_rectangle(170, 150, 370, 170, fill='red', outline="#004D40")
        hp_e2 = canvas.create_rectangle(390, 140, 590, 160, fill='black', outline="#004D40")
        hp_e = canvas.create_rectangle(390, 140, 590, 160, fill='red', outline="#004D40")
    elif opponent.name == 'Troll':
        opponent_image = troll_image
        canvas.coords(troll_image, 400, 170)
        hp_e2 = canvas.create_rectangle(390, 140, 590, 160, fill='black', outline="#004D40")
        hp_e = canvas.create_rectangle(390, 140, 590, 160, fill='red', outline="#004D40")
    elif opponent.name == 'Drakula':
        opponent_image = vampire_image
        canvas.coords(vampire_image, 400, 130)
        hp_e2 = canvas.create_rectangle(390, 270, 590, 290, fill='black', outline="#004D40")
        hp_e = canvas.create_rectangle(390, 270, 590, 290, fill='red', outline="#004D40")
        while True:
            coord = canvas.coords(vampire_image)
            if coord[1]==130 or coord[1]==100:
                yVelocity = -yVelocity
            canvas.move(vampire_image, 0, yVelocity)
            tk.update()
            time.sleep(0.05)

    while opponent.hp > 0:
        tk.update()
    else:
        if len(monsters) == 1:
            message.set('ПОБЕДА!')
            canvas.delete(hp_h)
            canvas.delete(hp_e)
            canvas.delete(hp_e2)
            canvas.delete(hp_h2)
            canvas.delete(opponent_image)
            message_enemy.set(f'{opponent.name} Мертв')
            return
        else:

            canvas.delete(hp_e)
            canvas.delete(hp_e2)
            canvas.delete(opponent_image)
            monsters.pop(0)
            enemy()

class Monster:
    def __init__(self, full_ehp: int, name: str, hp: int, mp: int, stats: dict):
        self.full_ehp = full_ehp
        self.name = name
        self.hp = hp
        self.mp = mp
        self.stats = stats
    def attack(self, target):
        import random
        number = random.randint(0, 100)
        crit_chance = random.randint(0, 100)
        if number > target.stats['agility']:
            if crit_chance >= 50:
                target.hp = target.hp - self.stats['strength'] * 20
                print(self.name, 'critical hits', target.name, 'and hits', self.stats['strength'] * 20,
                      'critical damage!')
                #message_enemy.set(f'{self.name} Сильно бьёт по {target.name} \nи наносит ему {self.stats['strength'] * 20}')
                x = (200 * target.hp) // target.full_hp
                canvas.coords(hp_h, 170, 150, 170 + x, 170)
            else:
                target.hp = target.hp - self.stats['strength'] * 10
                print(self.name, 'hits', target.name, 'and hits', self.stats['strength'] * 10, 'damage!')
                #message_enemy.set(f'{self.name} бьёт по {target.name} \nи наносит ему {self.stats['strength'] * 10}')
                x = (200 * target.hp) // target.full_hp
                canvas.coords(hp_h, 170, 150, 170 + x, 170)
        else:
            print(self.name, 'hits', target.name, 'and misses...')
           # message_enemy.set(f'{self.name} промахивается \nпо {target.name}...')
        if target.hp <= 0:
            a = StringVar(value='GAME OVER')
            b = Label(tk, textvariable=a, font=('Arial', 30))
            b.place(anchor="nw", x=130, y=70)
            canvas.delete(hero_image)
            canvas.delete(hp_h)
            canvas.delete(hp_h2)
            canvas.delete(hp_e)
            canvas.delete(hp_e2)
            canvas.delete(attack_button)
            canvas.delete(spell_button)
            canvas.delete(info_button)
            canvas.delete(start_button)
            canvas.create_image(225, 202, anchor=NW, image=rip_png)
            return
        # message.set('АЙ!')
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
        import random
        number = random.randint(0, 100)
        crit_chance = random.randint(0, 100)
        if target == "None":
            print('игрок не нажал на кнопку "играть"')
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
                canvas.coords(hp_e, 390, 140, 390 + x, 160)
                target.attack(allmight)
            else:
                target.hp = target.hp - self.stats['strength'] * 10
                print(self.name, 'hits', target.name, 'and hits', self.stats['strength'] * 10, 'damage!')
                message.set(f'{self.name} бьёт по {target.name} \nи наносит ему {self.stats['strength'] * 10}')
                message_enemy.set('АЙ!')
                x = (200 * target.hp) // target.full_ehp
                canvas.coords(hp_e, 390, 140, 390 + x, 160)
                target.attack(allmight)
        else:

            print(self.name, 'hits', target.name, 'and misses...')
            value = message.get()
            message.set(f'{self.name} промахивается по {target.name}...')
            message_enemy.set('Мозила!')
            target.attack(allmight)
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
                x = (200 * target.hp) // target.full_ehp
                canvas.coords(hp_e, 390, 140, 390 + x, 160)
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


fireball = Spell('fireball', 100, 'Mage cast a fireball! Awesome!', 'Damage', 100)
lightning = Spell('lightning', 150, 'Mage cast a lightning!', 'Damage', 150)
small_heal = Spell('small_heal', 50, 'Heals You!', 'Heal', 50)

allmight = Hero(500, 'Рыцарь', 500, 500, {'speed': 5, 'strength': 6, 'agility': 1, 'intelligence': 3, 'luck': 5}, [fireball])
ogr = Monster(100, 'Ogr', 100, 50, {'speed': 2, 'strength': 3, 'agility': 50, 'intelligence': 3, 'luck': 5}) #450
vampire = Monster(500, 'Drakula', 500, 300, {'speed': 5, 'strength': 10, 'agility': 0, 'intelligence': 5, 'luck': 0}) #500
troll = Monster(300, 'Troll', 300, 300, {'speed': 7, 'strength': 3, 'agility': 10, 'intelligence': 0, 'luck': 0}) #300
#__________________________________WINDOW__________________________________
tk = Tk()
tk.protocol('WM_DELETE_WINDOW', on_closing)
tk.title('Приложение')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=900, height=400, bd=0, highlightthickness=0)
canvas.pack()
#________________________________BACKGROUND_________________________________
canvas.create_line(0, 300, 900, 300, width=10)
canvas.create_rectangle(0, 300, 900, 600, fill='grey')
canvas.create_rectangle(0, 90, 110, 230, fill='black')

#______________________________CHARACTERS___________________________________
monsters = [ogr, troll, vampire]
hero_png = PhotoImage(file='Hero.png')
rip_png = PhotoImage(file='Rip.png')
ogr_png = PhotoImage(file='Ogr.png')
troll_png = PhotoImage(file='Trol.png')
vampire_png = PhotoImage(file='Vampir.png')
hero_image = canvas.create_image(200, 155, anchor=NW, image=hero_png)
ogr_image = canvas.create_image(400, 155, anchor=NW, image=ogr_png)
troll_image = canvas.create_image(550, 170, anchor=NW, image=troll_png)
vampire_image = canvas.create_image(700, 130, anchor=NW, image=vampire_png)
#__________________________________ANIMATIONS________________________________
yVelocity = 1


#__________________________________MESSAGES__________________________________
message = StringVar(value='Начнём игру?')
text_window = Label(tk, textvariable=message, font=('Arial', 15))
text_window.place(anchor="nw", x=130, y=70)
message_enemy = StringVar(value='[________]')
text_window2 = Label(tk, textvariable=message_enemy, font=('Arial', 15))
text_window2.place(anchor="nw", x=600, y=70)

#___________________________________BUTTONS__________________________________
opponent_game = "None"
start_btn = Button(tk, text="ИГРАТЬ!", command=lambda: enemy())
start_button = canvas.create_window(10, 100, width=90, anchor=NW, window=start_btn)
attack_btn = Button(tk, text="Атака", command=lambda: allmight.attack(opponent_game))
attack_button = canvas.create_window(10, 130, width=90, anchor=NW, window=attack_btn)
spell_btn = Button(text="Заклинание", command=lambda: allmight.cast(opponent_game, fireball))
spell_button = canvas.create_window(10, 160, width=90, anchor=NW, window=spell_btn)
info_btn = Button(text="Осмотреть", command=lambda: allmight.info_enemy(opponent_game))
info_button = canvas.create_window(10, 190, width=90, anchor=NW, window=info_btn)

tk.mainloop()