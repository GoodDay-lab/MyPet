class Pet:
    def __init__(self, name):
        self.name = name

        self.satiety = 100
        self.sleep = 100
        self.health = 100
        self.happy = 100
        self.purity = 100

        self.cash = 0
        self.level = 1
        self.exp = 0

        self.animation_stay = []
        self.animation_play = []
        self.animation_sleep = []

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

