import pygame
import numpy
import matplotlib.pyplot as plt

class points(pygame.sprite.Sprite):
    def __init__(self, color, height, width,degree):
        super().__init__()
  
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.pos_x, self.pos_y = screen_width/2, screen_height/2
        self.rect.center = ((self.pos_x,self.pos_y))
        self.degree = degree

    def update(self):
        global lengths
        self.pos_x += 1*numpy.cos(0.0174533*self.degree)
        self.pos_y += 1*numpy.sin(0.0174533*self.degree)
        self.rect.center = ((self.pos_x,self.pos_y))

        if pygame.sprite.spritecollideany(self, bg_list, pygame.sprite.collide_mask) or self.rect.x<0 or self.rect.x >screen_width or self.rect.y<0 or self.rect.y>screen_height:
            distance = numpy.sqrt((self.rect.x-screen_width/2)**2+(self.rect.y-screen_height/2)**2)
            data = [self.degree,distance]
            lengths.append(data)
            print(data)
            self.kill()

class bg(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
  
        self.image = pygame.image.load("images/Straight.png").convert() # Set Image here
        self.rect = self.image.get_rect()

  
pygame.init()
  
screen_width,screen_height = 683, 384
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Bonus Q1")
  
point_list = pygame.sprite.Group()
bg_list = pygame.sprite.Group()

for deg in range(1,361):
    point = points((255, 0, 0), 2,2,deg)
    point_list.add(point)

bg1 = bg()
bg_list.add(bg1)

for sprite in bg_list:
    sprite.mask = pygame.mask.from_threshold(sprite.image, pygame.Color('black'), (1, 1, 1, 255))
  
Running = True
clock = pygame.time.Clock()
lengths =[]
  
while Running:
    bg_list.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or len(lengths)==360:
            Running = False

    if len(lengths) == 360:
        x,y = [],[]

        for i in lengths:
            x.append(i[0])
            y.append(i[1])

        plt.scatter(x,y,label ="LiDar",color = 'k',linewidths = 0.01,s = 20)

        plt.xlabel('θ')
        plt.ylabel('Distance')
        plt.title("Bonus")
        plt.legend()
        plt.show()

    point_list.update()
    point_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)