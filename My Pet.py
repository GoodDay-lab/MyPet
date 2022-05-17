import pygame
from os import listdir
from time import time

pygame.init()
X, Y = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Мой питомец')
clock = pygame.time.Clock()

running = True
FPS = 60

c = pygame.Rect(X * 0.1, Y * 0.1, X * 0.4, Y * 0.4)
sprites = {}


class Animation(pygame.sprite.Sprite):
    def __init__(self, images, time_interval, index=0):
        super(Animation, self).__init__()
        self.images = images
        self.image = self.images[0]
        self.time_interval = time_interval
        self.index = index
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
            x, y = X // 1.5, Y
        if file == 'маленький корм.png':
            x, y = X // 6.5, Y // 5.5
        if file == 'корм средний.png':
            x, y = X // 6.5, Y // 5.5
        if file == 'большой корм.png':
            x, y = X // 6.5, Y // 5.5
        if file == 'открытые глаза рисунок.png':
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
        sprites[file] = pygame.transform.scale(pygame.image.load(path + file), (x, y))


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

        self.status = 0
        self.anims = kwargs

    def play(self):
        set_params(pet, health=-5, sleep=-10, satiety=-20, purity=-10, happy=20)

    def sleep(self):
        set_params(pet, health=-2, sleep=100, satiety=-50, purity=-5, happy=-10)

    def eat(self, count):
        set_params(pet, sleep=-10, satiety=count)

    def walk(self):
        set_params(pet, sleep=-50, satiety=-20, purity=0, happy=50)

    def hospital(self):
        set_params(pet, health=100)

    def set_status(self):
        pass

    def draw(self, screen):
        screen.blit(self.anims['open_eyes'], (X * 0.3, Y * 0.6))


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


# class Hood:
#     def __init__(self, x, y, width, height, text, icon):


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

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_back.check_press(pygame.mouse.get_pos())
        update_screen()


def go_shop(screen):
    time_now = time()
    for i in range(255):
        screen.fill((0, 0, 0))
        update_screen()
    while time() - time_now < 120:
        screen.blit(sprites['магазин.png'], (X // 6, 0)) and (X // 1.5, Y)
        screen.blit(sprites['маленький корм.png'], (X * 0.2, Y * 0.25)) and (X // 6.5, Y // 5.5)
        screen.blit(sprites['корм средний.png'], (X * 0.4, Y * 0.25)) and (X // 6.5, Y // 5.5)
        screen.blit(sprites['большой корм.png'], (X * 0.6, Y * 0.25)) and (X // 2.5, Y // 4.5)
        screen.blit(sprites['кнопка back.png'], (X * 0.16, Y * 0.08)) and (X // 10, Y // 8)
        button_back.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_back.check_press(pygame.mouse.get_pos())
        update_screen()


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
        screen.blit(sprites['открытые глаза рисунок.png'], (X * 0.35, Y * 0.6))
        screen.blit(sprites['кнопка play.png'], (X * 0.15, Y * 0.2))
        screen.blit(sprites['кнопка walk.png'], (X * 0.15, Y * 0.35))
        screen.blit(sprites['кнопка hospital.png'], (X * 0.15, Y * 0.5))
        screen.blit(sprites['кнопка kitchen.png'], (X * 0.15, Y * 0.65))
        button_sleep.draw(screen)
        button_walk.draw(screen)
        button_hospital.draw(screen)
        button_hospital.draw(screen)
        button_pc.draw(screen)

        # anim.update(0.05)
        # screen.blit(anim.image, (0, 0))

        # home.update(screen)
        # pet.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print('click')
                button_sleep.check_press(pygame.mouse.get_pos())
                button_walk.check_press(pygame.mouse.get_pos())
                button_hospital.check_press(pygame.mouse.get_pos())
                button_kitchen.check_press(pygame.mouse.get_pos())
                button_pc.check_press(pygame.mouse.get_pos())
                button_back.check_press(pygame.mouse.get_pos())

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
# pet = Pet('Бобик', close_eyes=dog_close_eyes, open_eyes=dog_open_eyes, up_tail=dog_Up_tail)
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

if __name__ == '__main__':
    main(screen)