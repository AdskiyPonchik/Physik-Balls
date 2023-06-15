import pygame, random, math
pygame.init()
clock = pygame.time.Clock()
black = (0,0,0)
done = False
class Preparing():
    width = 1500
    height = 900
    title = "Физические мячики"
    window = pygame.display.set_mode([width, height])
    pygame.display.set_caption(title)
    refresh_rate = 120
    speedx = 10
    speedy = 10
    m = 1.0
    Color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
class Box():
    x = (random.randint(10, 100))
    y = x
    dx, dy = x, y
    def __init__(self,color,window,speedx,speedy):
        self.color = color
        self.black = black
        self.window = window
        self.speedx = speedx
        self.speedy = speedy
    def Draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.dx, self.dy))
    def Updating(self):
        self.x += self.speedx
        self.y += self.speedy
        if self.x >= (Preparing.width - self.dx) or self.x <= 0:
            self.speedx *= -1
        if self.y >= (Preparing.height - self.dy) or self.y <= 0:
            self.speedy *= -1
class Circle():
    x = (random.randint(500, 1000))
    y = (random.randint(200, 500))
    rad = 60

    def __init__(self, x: int, y: int, color: list, window, speedx: int, speedy: int):
        self.x = x
        self.y = y
        self.color = color
        self.black = black
        self.window = window
        self.speedx = speedx
        self.speedy = speedy

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.x, self.y), self.rad)

    def updating(self):
        self.x += self.speedx
        self.y += self.speedy
        if self.x >= (Preparing.width - self.rad) or self.x <= 0+self.rad:
            self.speedx *= -1
        if self.y >= (Preparing.height - self.rad) or self.y <= 0+self.rad:
            self.speedy *= -1

    def collide(self, v1x, v1y, v2x, v2y) -> None:
        v1x_next = ()

#box = Box([random.randint(0, 255) for _ in range(3) ], Preparing.window,Preparing.speedx,Preparing.speedy)
ball1 = Circle(500, 200, [random.randint(0, 255) for _ in range(3)], Preparing.window, random.randint(5, 15), random.randint(5, 15))
ball2 = Circle(200, 500, [random.randint(0, 255) for _ in range(3)], Preparing.window, random.randint(5, 15), random.randint(5, 15))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    Preparing.window.fill(black)
    distance = math.sqrt((ball1.x - ball2.x) ** 2 + (ball1.y - ball2.y) ** 2)
    if distance < (ball1.rad+ball2.rad):
        """Вычисления выполнены с помощью формулы созранения импульса и энергии. Закон сохранения импульса: 
        взимодействие двух тел означает равенство их импульсов до и после взаимодействия. Импульс = произведение массы 
        тела на его скорость. Таким образом, после столкновения сумма импульсов этих двух мячиков должна равняться сумме 
        импульсов мячиков до столкновения. Закон сохранения энергии гласит, что взаимодействие двух тел не изменяет их 
        суммарную энергию. Получается, что сумма кинетических энергий двух мячиков до столкновения, должна быть такой же 
        и после столкновения.
        """
        dx, dy = (ball1.x - ball2.x) / distance, (ball1.y - ball2.y) / distance
        v1, v2 = math.sqrt(ball1.speedx ** 2 + ball1.speedy ** 2), math.sqrt(ball2.speedx ** 2 + ball2.speedy ** 2)
        phi1, phi2 = math.atan2(ball1.speedy, ball1.speedx), math.atan2(ball2.speedy, ball2.speedx)
        m1, m2 = 1, 1
        vx1, vy1 = v1 * math.cos(phi1 - math.atan2(dy, dx)), v1 * math.sin(phi1 - math.atan2(dy, dx))
        vx2, vy2 = v2 * math.cos(phi2 - math.atan2(dy, dx)), v2 * math.sin(phi2 - math.atan2(dy, dx))
        v1x, v2x = ((m1 - m2) * vx1 + (m2 + m2) * vx2) / (m1 + m2), ((m1 + m1) * vx1 + (m2 - m1) * vx2) / (m1 + m2)
        v1y, v2y = vy1, vy2
        ball1.speedx = math.cos(math.atan2(dy, dx)) * v1x + math.cos(math.pi / 2 + math.atan2(dy, dx)) * v1y
        ball1.speedy = math.sin(math.atan2(dy, dx)) * v1x + math.sin(math.pi / 2 + math.atan2(dy, dx)) * v1y
        ball2.speedx = math.cos(math.atan2(dy, dx)) * v2x + math.cos(math.pi / 2 + math.atan2(dy, dx)) * v2y
        ball2.speedy = math.sin(math.atan2(dy, dx)) * v2x + math.sin(math.pi / 2 + math.atan2(dy, dx)) * v2y

    ball1.draw()
    ball2.draw()
    ball1.updating()
    ball2.updating()
    pygame.display.flip()

    clock.tick(Preparing.refresh_rate)
pygame.quit()