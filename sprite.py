import pygame
import random
pygame.init()
spritecolor_changeevent=pygame.USEREVENT+1
backgroundcolor_changeevent=pygame.USEREVENT+2
blue=pygame.Color("blue")
lightblue=pygame.Color("lightblue")
darkblue=pygame.Color("darkblue")
red=pygame.Color("red")
orange=pygame.Color("orange")
yellow=pygame.Color("yellow")
green=pygame.Color("green")
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit=False
        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity[0]=-self.velocity[0]
            boundary_hit=True
        if self.rect.top<=0 or self.rect.bottom>=400:
            self.velocity[1]=-self.velocity[1]
            boundary_hit=True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(spritecolor_changeevent))
            pygame.event.post(pygame.event.Event(backgroundcolor_changeevent))
    def changecolor(self):
        self.image.fill(random.choice([red,orange,yellow,green]))
def changebgcolor():
    global bg_color
    bg_color=random.choice([blue,lightblue,darkblue])
allspriteslist=pygame.sprite.Group()
sp1=Sprite(red,20,30)
sp1.rect.x=random.randint(0,480)
sp1.rect.y=random.randint(0,400)
allspriteslist.add(sp1)
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("colourful sprite")
bg_color=blue
screen.fill(bg_color)
exit=False
clock=pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
        elif event.type==spritecolor_changeevent:
            sp1.changecolor()
        elif event.type==backgroundcolor_changeevent:
            changebgcolor()
    allspriteslist.update()
    screen.fill(bg_color)
    allspriteslist.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()