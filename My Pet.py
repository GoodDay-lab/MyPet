import pygame
from os import listdir, stat
from time import time

from movement import *

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
X, Y = screen.get_size()
pygame.display.set_caption('Мой питомец')
clock = pygame.time.Clock()

running = True
FPS = 60

c = pygame.Rect(X * 0.1, Y * 0.1, X * 0.4, Y * 0.4)
sprites = {}


DOG_CRDS_MAIN = (X * 0.35, Y * 0.6)
DOG_CRDS_KTCH = (X * 0.35, Y * 0.6)


class Animation(pygame.sprite.Sprite):
    def __init__(self, images, time_interval, crds, index=0):
        super(Animation, self).__init__()
        self.images = images
        self.image = self.images[0]
        self.time_interval = time_interval
        self.index = index
        self.crds = crds
        self.timer = 0

    def update(self, seconds, reverse=False):
        self.timer += seconds
        if self.timer >= self.time_interval:
            self.image = self.images[self.index]
            if reverse:
                self.image = pygame.transform.flip(self.image, True, False)
            self.index = (self.index + 1) % len(self.images)
            self.timer = 0


def load_sprites():
    global sprites
    path = 'sprites/'
    for file in listdir(path):
        x, y = X, Y
        if file == 'фон гостинная.png':
            x, y = X // 1.5, Y
        if file == 'лежанка.png':
            x, y = X // 4.5, Y // 3.5
        if file == 'пк.png':
            x, y = X // 5, Y // 4
        if file == 'задачи.png':
            x, y = X // 12, Y // 6
        if file == 'фон кухня.png':
            x, y = X // 1.5, Y
        if file == 'пустая миска.png':
            x, y = X // 6.5, Y // 5.5
        # if file == 'полная миска.png':
        #     x, y = X // 6.5, Y // 5.5
        if file == 'магазин.png':
            x, y = X // 2, Y
        if file == 'маленький корм.png':
            x, y = X // 6.5, Y // 5.5
        if file == 'корм средний.png':
            x, y = X // 6.5, Y // 5.5
        if file == 'большой корм.png':
            x, y = X // 6.5, Y // 5.5
        if file == 'открытые глаза.png':
            x, y = X // 3.5, Y // 2.5
        if file == 'кнопка play.png':
            x, y = X // 10, Y // 8
        if file == 'кнопка walk.png':
            x, y = X // 10, Y // 8
        if file == 'кнопка hospital.png':
            x, y = X // 10, Y // 8
        if file == 'кнопка kitchen.png':
            x, y = X // 10, Y // 8
        if file == 'кнопка back.png':
            x, y = X // 10, Y // 8
        if file == 'корзина.png':
            x, y = X // 10, Y // 8
        if file == 'сердце.png':
            x, y = X // 10, Y // 8
        if file == 'куриная ножка.png':
            x, y = X // 10, Y // 8
        if file == 'кровать.png':
            x, y = X // 10, Y // 8
        if file == 'смайлик.png':
            x, y = X // 10, Y // 8
        if file == 'ухо левое.png':
            x, y = X // 3.5, Y // 2.5
        if file == 'ухо правое.png':
            x, y = X // 3.5, Y // 2.5
        if file == 'закрытые глаза.png':
            x, y = X // 3.5, Y // 2.5
        if file == 'поднятый хвост.png':
            x, y = X // 3.5, Y // 2.5
        if file == 'мяч между лап.png':
            x, y = X // 3.5, Y // 2.5
        if file == 'мяч в левой.png':
            x, y = X // 3.5, Y // 2.5
        if file == 'мяч в правой.png':
            x, y = X // 3.5, Y // 2.5
        sprites[file] = pygame.transform.scale(pygame.image.load(path + file), (x, y))


load_sprites()

dog_sitting = Animation([sprites['закрытые глаза.png'], sprites['открытые глаза.png'], sprites['поднятый хвост.png'],
                         sprites['открытые глаза.png']], 1, DOG_CRDS_MAIN)
dog_ears = Animation([sprites['закрытые глаза.png'], sprites['открытые глаза.png'], sprites['поднятый хвост.png']],
                     1, DOG_CRDS_KTCH)
dog_play = Animation([sprites['мяч в левой.png'], sprites['мяч в правой.png']],
                     1, DOG_CRDS_MAIN)


class Pet:
    def __init__(self, name, **kwargs):
        self.name = name

        self.satiety = 100
        self.sleep = 100
        self.health = 100
        self.happy = 100
        self.purity = 100

        self.cash = 0
        self.level = 1
        self.exp = 0

        self.status = 'dog_sitting'
        self.anims = kwargs
        self.playing = False
        self.actions = {
            'dog_sitting': dog_sitting,
            'dog_ears': dog_ears,
            'dog_play': dog_play
        }

    def play(self):
        set_params(self, health=-5, sleep=-10, satiety=-20, happy=20)

    def sleep(self):
        set_params(self, health=-2, sleep=100, satiety=-50, happy=-10)

    def eat(self, count):
        set_params(self, sleep=-10, satiety=count)

    def walk(self):
        set_params(self, sleep=-50, satiety=-20, purity=0, happy=50)

    def hospital(self):
        set_params(self, health=100)

    def set_status(self):
        pass

    def draw(self, screen):
        screen.blit(self.actions[self.status].image, self.actions[self.status].crds)


class Button:
    def __init__(self, text, x, y, width, height, action, texture_still, texture_active):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.action = action
        self.texture_still = texture_still
        self.texture_active = texture_active

    def draw(self, screen):
        screen.blit(self.texture_still, (self.x, self.y))

    def press(self, screen):
        screen.blit(self.texture_active, (self.x, self.y))

    def check_press(self, pos):
        if (self.x <= pos[0] <= self.x + self.width) and (self.y <= pos[1] <= self.y + self.height):
            self.action(screen)


class Indicator:
    def __init__(self, x, y, width, height, text, icon):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.icon = pygame.transform.scale(icon, (width // 2, height))
        self.font = pygame.font.SysFont('Times New Roman', 20)

    def draw(self, screen):
        screen.blit(self.icon, (self.x, self.y))
        screen.blit(self.font.render(f'{self.text}%', True, (0, 0, 0)), (self.x + self.width // 2, self.y + self.height // 3))


class Home:
    def __init__(self, **kwargs):
        self.pictures = kwargs
        print(self.pictures)

    def update(self, screen):
        for picture in self.pictures:
            screen.blit(self.pictures[picture][0], self.pictures[picture][1])


def set_params(obj: Pet, health=0, sleep=0, satiety=0, purity=0, happy=0):
    if health > 0:
        if obj.health + health > 100:
            obj.health = 100
        else:
            obj.health += health
    if health < 0:
        if obj.health - health < 0:
            obj.health = 0
        else:
            obj.health -= health

    if sleep > 0:
        if obj.sleep + sleep > 100:
            obj.sleep = 100
        else:
            obj.sleep += sleep
    if sleep < 0:
        if obj.sleep - sleep < 0:
            obj.sleep = 0
        else:
            obj.sleep -= sleep

    if satiety > 0:
        if obj.satiety + satiety > 100:
            obj.satiety = 100
        else:
            obj.satiety += satiety
    if satiety < 0:
        if obj.satiety - satiety < 0:
            obj.satiety = 0
        else:
            obj.satiety -= satiety

    if purity > 0:
        if obj.purity + purity > 100:
            obj.purity = 100
        else:
            obj.purity += purity
    if purity < 0:
        if obj.purity - purity < 0:
            obj.purity = 0
        else:
            obj.purity -= purity

    if happy > 0:
        if obj.happy + happy > 100:
            obj.happy = 100
        else:
            obj.happy += happy
    if happy < 0:
        if obj.happy - happy < 0:
            obj.happy = 0
        else:
            obj.happy -= happy


def update_screen():
    pygame.display.flip()
    clock.tick(FPS)


def go_sleep(screen):
    time_now = time()
    for i in range(255):
        screen.fill((255 - i, 255 - i, 255 - i))
        update_screen()
    while time() - time_now < 3:
        screen.fill((0, 0, 0))
        update_screen()
    for i in range(255):
        screen.fill((i, i, i))
        update_screen()

    print(pet.sleep)
    set_params(pet, sleep=100)
    print(pet.sleep)
    indicator_sleep.text = pet.sleep
    print(indicator_sleep.text)


def go_walk(screen):
    time_now = time()
    for i in range(255):
        screen.fill((i, i, i))
        update_screen()
    while time() - time_now < 3:
        screen.fill((0, 0, 0))
        update_screen()
    for i in range(255):
        screen.fill((255, 255, 255))
        update_screen()


def go_hospital(screen):
    time_now = time()
    for i in range(255):
        screen.fill((0, 0, 0))
        update_screen()
    while time() - time_now < 3:
        screen.fill((255, 255, 255))
        update_screen()
    for i in range(255):
        screen.fill((i, i, i))
        update_screen()


def go_kitchen(screen):
    time_now = time()
    for i in range(255):
        screen.fill((0, 0, 0))
        update_screen()
    while time() - time_now < 120:
        screen.blit(sprites['фон кухня.png'], (X // 6.5, 0)) and (X // 1.5, Y)
        screen.blit(sprites['пустая миска.png'], (X * 0.2, Y * 0.81)) and (X // 6.5, Y // 5.5)
        screen.blit(sprites['кнопка back.png'], (X * 0.16, Y * 0.08)) and (X // 10, Y // 8)
        button_back.draw(screen)
        dog_ears.update(0.05)
        screen.blit(dog_ears.image, DOG_CRDS_KTCH)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_back.check_press(pygame.mouse.get_pos())
        update_screen()


def go_shop(screen):
    
    class ShopProduct(pygame.sprite.Sprite):
        def __init__(self, image):
            super().__init__()
            self.shop = None
            self.image = image
            self.rect = self.image.get_rect()
        
        def event_hook(self, e):
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1 and self.rect.collidepoint(e.pos):
                self.shop.choose(self)
                move = Movement(self, (4, -math.atan2(Y - self.rect.centery, X * 0.5 - self.rect.centerx)), 
                                (8, math.pi / 2), limit_func=lambda move: move.obj.rect.center[1] >= Y - 50)
                moves.add(move)
    
    class ShopProducts(pygame.sprite.Group):
        def __init__(self, *products):
            super().__init__(*products)
            self.table = [[0, 0, 0, 0], [0, 0, 0, 0]]
            self.goods = []
        
        def add_product(self, product):
            for ri, row in enumerate(self.table):
                if not all(row):
                    for ci, col in enumerate(row):
                        if col:
                            continue
                        self.table[ri][ci] = product
                        product.rect.x = (ci + 1) * (X) / 6
                        product.rect.y = (ri + 1) * (Y) / 4
                        product.shop = self
                        self.add(product)
                        return
            
        def choose(self, obj):
            if not any(obj in l for l in self.table):
                return
            self.goods.append(obj)



    moves = Movements()
    
    static = pygame.sprite.Group()
    background = pygame.sprite.Sprite(static)
    background.rect = pygame.Rect(0, 0, X * 1, Y)
    background.image = pygame.transform.scale(sprites['магазин.png'], background.rect.size)
    
    products = ShopProducts()
    backpack = pygame.sprite.Sprite(products)
    backpack.rect = pygame.Rect(X * 0.20, Y * 0.80, X * 0.6, Y * 0.2)
    products.add_product(ShopProduct(sprites['маленький корм.png']))
    products.add_product(ShopProduct(sprites['корм средний.png']))
    products.add_product(ShopProduct(sprites['большой корм.png']))
    # products.add_product(ShopProduct(sprites['большой корм.png']))
    products.add_product(ShopProduct(sprites['маленький корм.png']))
    # products.add_product(ShopProduct(sprites['большой корм.png']))
    # products.add_product(ShopProduct(sprites['большой корм.png']))
    # products.add_product(ShopProduct(sprites['большой корм.png']))
    # products.add_product(ShopProduct(sprites['большой корм.png']))
    # products.add_product(ShopProduct(sprites['большой корм.png']))
    backpack.image = pygame.transform.scale(sprites['корзина.png'], backpack.rect.size)
    
    time_now = time()
    for i in range(2):
        screen.fill((0, 0, 0))
        update_screen()
    while time() - time_now < 120:
        static.draw(screen)
        products.draw(screen)
        screen.blit(sprites['кнопка back.png'], (X * 0.16, Y * 0.08)) and (X // 10, Y // 8)
        button_back.draw(screen)
        moves.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_back.check_press(pygame.mouse.get_pos())
                for prod in products:
                    if hasattr(prod, "event_hook"):
                        prod.event_hook(event)
        update_screen()


def go_play(screen):
    if pet.playing is True:
        pet.status = 'dog_play'
    update_screen()
    print(1)


def main(screen):
    global running
    while running:
        screen.fill((0, 0, 0))
        screen.blit(sprites['фон гостинная.png'], (X // 6.5, 0))
        screen.blit(sprites['лежанка.png'], (X * 0.17, Y * 0.734))
        screen.blit(sprites['пк.png'], (X * 0.58, Y * 0.5))
        screen.blit(sprites['задачи.png'], (X * 0.593, Y * 0.75))
        # screen.blit(sprites['фон кухня.png'], (X // 6.5, 0))
        # screen.blit(sprites['пустая миска.png'], (X * 0.2, Y * 0.81))
        # screen.blit(sprites['полная миска.png'], (X * 0.2, Y * 0.81))
        # screen.blit(sprites['магазин.png'], (X // 6, 0))
        # screen.blit(sprites['маленький корм.png'], (X * 0.2, Y * 0.25))
        # screen.blit(sprites['корм средний.png'], (X * 0.4, Y * 0.25))
        # screen.blit(sprites['большой корм.png'], (X * 0.6, Y * 0.25))
        # screen.blit(sprites['открытые глаза.png'], (X * 0.35, Y * 0.6))
        # screen.blit(sprites['закрытые глаза.png'], (X * 0.35, Y * 0.6))
        # screen.blit(sprites['ухо левое.png'], (X * 0.35, Y * 0.6))
        # screen.blit(sprites['ухо правое.png'], (X * 0.35, Y * 0.6))
        # screen.blit(sprites['поднятый хвост.png'], (X * 0.35, Y * 0.6))
        # screen.blit(sprites['мяч между лап.png'], (X * 0.35, Y * 0.6))
        # screen.blit(sprites['мяч в левой.png'], (X * 0.35, Y * 0.6))
        # screen.blit(sprites['мяч в правой.png'], (X * 0.35, Y * 0.6))
        dog_sitting.update(0.1)
        screen.blit(sprites['кнопка play.png'], (X * 0.15, Y * 0.2))
        screen.blit(sprites['кнопка walk.png'], (X * 0.15, Y * 0.35))
        screen.blit(sprites['кнопка hospital.png'], (X * 0.15, Y * 0.5))
        screen.blit(sprites['кнопка kitchen.png'], (X * 0.15, Y * 0.65))


        button_sleep.draw(screen)
        button_walk.draw(screen)
        button_hospital.draw(screen)
        button_hospital.draw(screen)
        button_pc.draw(screen)
        button_play.draw(screen)

        indicator_HP.draw(screen)
        indicator_eat.draw(screen)
        indicator_sleep.draw(screen)
        indicator_happy.draw(screen)

        dog_sitting.update(0.05)
        screen.blit(dog_sitting.image, DOG_CRDS_MAIN)

        go_play(screen)
        # home.update(screen)
        pet.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_play.check_press(pygame.mouse.get_pos()):
                    pet.playing = True
                print('click')
                button_sleep.check_press(pygame.mouse.get_pos())
                button_walk.check_press(pygame.mouse.get_pos())
                button_hospital.check_press(pygame.mouse.get_pos())
                button_kitchen.check_press(pygame.mouse.get_pos())
                button_pc.check_press(pygame.mouse.get_pos())
                button_back.check_press(pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONUP:
                pet.playing = False

            if event.type == pygame.KEYDOWN:
                print('key')
                if event.key == pygame.K_s:
                    print('s')
                    go_sleep(screen)
                    go_walk(screen)
                    go_hospital(screen)
                    go_kitchen(screen)
                    go_shop(screen)
        update_screen()


load_sprites()
pet = Pet('Бобик')# , close_eyes=dog_close_eyes, open_eyes=dog_open_eyes, up_tail=dog_Up_tail)
# home = Home(**items)

button_sleep = Button(text='', x=X * 0.17, y=Y * 0.734, height=Y // 3.5, width=X // 4.5, action=go_sleep,
                      texture_active=sprites['лежанка.png'], texture_still=sprites['лежанка.png'])
button_walk = Button(text='', x=X * 0.15, y=Y * 0.35, height=Y // 8, width=X // 10, action=go_walk,
                     texture_active=sprites['кнопка walk.png'], texture_still=sprites['кнопка walk.png'])
button_hospital = Button(text='', x=X * 0.15, y=Y * 0.5, height=Y // 8, width=X // 10, action=go_hospital,
                         texture_active=sprites['кнопка hospital.png'], texture_still=sprites['кнопка hospital.png'])
button_kitchen = Button(text='', x=X * 0.15, y=Y * 0.65, height=Y // 8, width=X // 10, action=go_kitchen,
                        texture_active=sprites['кнопка kitchen.png'], texture_still=sprites['кнопка kitchen.png'])
button_pc = Button(text='', x=X * 0.58, y=Y * 0.5, height=Y // 4, width=X // 5, action=go_shop,
                   texture_active=sprites['пк.png'], texture_still=sprites['пк.png'])
button_back = Button(text='', x=X * 0.16, y=Y * 0.08, height=Y // 8, width=X // 10, action=main,
                     texture_active=sprites['кнопка back.png'], texture_still=sprites['кнопка back.png'])
button_play = Button(text='', x=X * 0.15, y=Y * 0.2,height=Y // 8, width=X // 10, action=go_play,
                     texture_active=sprites['кнопка play.png'], texture_still=sprites['кнопка play.png'])

indicator_HP = Indicator(X * 0.16, Y * 0.01, X // 25, Y // 25, pet.health, sprites['сердце.png'])
indicator_eat = Indicator(X * 0.22, Y * 0.01, X // 25, Y // 25, pet.satiety, sprites['куриная ножка.png'])
indicator_sleep = Indicator(X * 0.28, Y * 0.01, X // 25, Y // 25, pet.sleep, sprites['кровать.png'])
indicator_happy = Indicator(X * 0.34, Y * 0.01, X // 25, Y // 25, pet.happy, sprites['смайлик.png'])


if __name__ == '__main__':
    main(screen)
