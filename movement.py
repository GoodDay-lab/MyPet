import math
import pygame


class Movement:
    def __init__(self, obj, start_force, *forces, limit_func=None):
        self.time = 0
        self.interval = 1 / 30
        self.time += self.interval * 3
        self.obj = obj
        self.forces = []
        self.start_force = start_force
        self.limit_func = limit_func
        
        for force in forces:
            self.forces.append({
                'value': force[0],
                'angle': force[1]
            })
    
    def update(self):
        if self.limit_func:
            if self.limit_func(self):
                return
        self.time += self.interval
        start_force = self.start_force
        move = [0, 0]
        
        for force in self.forces:
            move[0] += force['value'] * math.cos(force['angle'])
            move[1] += force['value'] * math.sin(force['angle'])

        if hasattr(self.obj, "rect"):
            self.obj.rect.x += start_force[0] * math.cos(start_force[1]) * self.time + move[0] * math.pow(self.time, 2) / 2
            self.obj.rect.y += start_force[0] * math.sin(start_force[1]) * self.time + move[1] * math.pow(self.time, 2) / 2
        else:
            print("[WARNING] object %s hasn't a neccessary attribute 'rect'" % self.obj.__name__)


class Movements:
    def __init__(self, *movements):
        self.l = []
        
        for move in movements:
            self.add(move)
        
    def add(self, movement):
        if type(movement) == Movement:
            self.l.append(movement)
    
    def update(self):
        for movement in self.l:
            movement.update()
                

def testing():
    import pygame
    import random
    
    pygame.init()
    fps = 60
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    movements = Movements()
    
    class Ball():
        def __init__(self, pos):
            size = 5
            self.rect = pygame.Rect(*pos, size * 2, size * 2)
            self.rect.x -= size
            self.rect.y -= size
            movements.add(Movement(self, (random.random() * 2 + 1, (random.random() + 3) * 2 *math.pi),
                                   (3, math.pi / 2), (25, math.pi), (15, math.pi)))
    
    balls = []
    is_running = True
    while is_running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                is_running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                for _ in range(50):
                    balls.append(Ball(e.pos))
            elif e.type == pygame.MOUSEMOTION:
                for _ in range(3):
                    balls.append(Ball(e.pos))
        
        screen.fill('black')
        
        for ball in balls:
            if ball.rect.y > 900:
                balls.remove(ball)
            pygame.draw.ellipse(screen, 'white', ball.rect)
            
        pygame.display.flip()
        clock.tick(fps)
        movements.update()


if __name__ == '__main__':
    testing()
