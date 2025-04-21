from pygame import *
from random import *
class Sprite(sprite.Sprite):
    def __init__(self, Image, xize, yize, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(Image), (xize, yize))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        if keys_pressed[K_a] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x <= 700:
            self.rect.x += self.speed
    def fire(self):
        Bullet = bullet('bullet.png', 15, 20, 15, self.rect.centerx, self.rect.top)
        Bullets.add(Bullet)
    def Boom_fire(self):
        global count_boom
        if count_boom > 0:
            Boom_Bullet = bullet('boo_bullet.png', 15, 20, 15, self.rect.centerx, self.rect.top)
            Boom_Bullets.add(Boom_Bullet)
            count_boom -= 1
    def otris(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

lost = 0
score = 0
class Enemy(Sprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= game_width:
            self.rect.x = randint(80, game_width - 80)
            self.rect.y = 0
            lost += 1
class bullet(Sprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y == 0:
            self.kill()
        

game_width = 700
game_hight = 500
window = display.set_mode((game_width, game_hight))
display.set_caption("Шутер")
background = transform.scale(image.load('galaxy.jpg'), (game_width,game_hight))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire = mixer.Sound('fire.ogg')
rocket = Sprite('rocket.png', 80, 100, 10, 350, 400)
rockat = sprite.Group()
rockat.add(rocket)
monster = Enemy('ufo.png', 80, 50, randint(1, 5), randint(80, game_width - 80), -40)
monster1 = Enemy('ufo.png', 80, 50, randint(1, 5), randint(80, game_width - 80), -40)
monster2 = Enemy('ufo.png', 80, 50, randint(1, 5), randint(80, game_width - 80), -40)
monster3 = Enemy('ufo.png', 80, 50, randint(1, 5), randint(80, game_width - 80), -40)
monster4 = Enemy('ufo.png', 80, 50,randint(1, 5), randint(80, game_width - 80), -40)
monsters = sprite.Group()
monsters.add(monster)
monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)
asteroid1 = Enemy('asteroid.png', 60, 60, randint(1, 3), randint(80, game_width - 80), -40)
asteroid2 = Enemy('asteroid.png', 60, 60, randint(1, 3), randint(80, game_width - 80), -40)
asteroid3 = Enemy('asteroid.png', 60, 60, randint(1, 3), randint(80, game_width - 80), -40)
asteroids = sprite.Group()
asteroids.add(asteroid1)
asteroids.add(asteroid2)
asteroids.add(asteroid3)
font.init()
font1 = font.SysFont("Arial", 23)
font2 = font.SysFont('Arial', 90)
Bullets = sprite.Group()
Boom_Bullets = sprite.Group()
lose = font2.render("YOU LOSE!", True, (215, 0, 0))
win = font2.render("YOU WIN!", True, (0, 215, 0))
live = 5
start = font2.render("ШУТЕР!", True, (255, 255, 255))
migalka = font1.render('Нажмите кнопку:"E" для запуска игры', True, (255, 255, 255))
d = 5
count_boom = 10
game = True
finish = True
Clock = time.Clock()
FPS = 60
while game:
    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
        if keys_pressed[K_e]:
            finish = False
            rocket.rect.x = 350
            rocket.rect.y = 400
            live = 5
            count_boom = 10
            if d == 5:
                d -= 5
            for r in monsters:
                r.rect.y = 0
                r.rect.x = randint(80, game_width - 80)
            for p in asteroids:
                p.rect.y = 0
                p.rect.x = randint(80, game_width - 80)
            lost = 0
            score = 0
        if keys_pressed[K_r] and finish != True:
            if count_boom != 0:
                rocket.Boom_fire()
                fire.play()
        elif e.type == KEYDOWN:
            if e.key == K_SPACE and finish != True:
                rocket.fire()
                fire.play()
    if sprite.groupcollide(monsters, rockat, True, False):
            monster4 = Enemy('ufo.png', 80, 50,randint(1, 5), randint(80, game_width - 80), -40)
            monsters.add(monster4)
            live -= 1
    if sprite.groupcollide(asteroids, rockat, True, False):
        asteroid1 = Enemy('asteroid.png', 60, 60, randint(1, 3), randint(80, game_width - 80), -40)
        asteroids.add(asteroid1)
        live -= 1
    if lost >= 5 or live <= 0: 
        finish = True
        window.blit(background, (0, 0))
        window.blit(lose, (170, 220))
    if score >= 10:
        finish = True
        window.blit(background, (0, 0))
        window.blit(win, (170, 220))
    if d == 5:
        window.blit(background, (0, 0))
        window.blit(start, (200, 100))
        window.blit(migalka,(125, 300))
    if finish != True:
        text1 = font1.render('счёт:' + str(score), 1, (255,255,255))
        text2 = font1.render('пропущенно:' + str(lost), 1, (255,255,255))
        text3 = font1.render('осталось жизней:' + str(live), 1, (0, 255, 0))
        text4 = font1.render('взрывных патронов:' + str(count_boom), 1, (255, 255, 255))
        window.blit(background, (0, 0))
        window.blit(text2, (10, 50))
        window.blit(text1, (10, 20))
        window.blit(text3, (10, 110))
        window.blit(text4, (10, 80))
        rocket.otris()
        monsters.draw(window)
        asteroids.draw(window)
        Bullets.draw(window)
        Boom_Bullets.draw(window)
        Boom_Bullets.update()
        Bullets.update()
        monsters.update()
        asteroids.update()
        rocket.update()
        if sprite.groupcollide(monsters, Bullets, True, True) or sprite.groupcollide(monsters, Boom_Bullets, True, True):
            monster4 = Enemy('ufo.png', 80, 50,randint(1, 5), randint(80, game_width - 80), -40)
            monsters.add(monster4)
            score += 1
        if sprite.groupcollide(asteroids, Bullets, False, True):
            pass
        if sprite.groupcollide(asteroids, Boom_Bullets, True, True):
            asteroid1 = Enemy('asteroid.png', 60, 60, randint(1, 3), randint(80, game_width - 80), -40)
            asteroids.add(asteroid1)
        
    display.update()
    Clock.tick(FPS)