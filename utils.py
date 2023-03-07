'''
Utilitaires
'''

import random
import pygame

# Quelques couleurs...
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)


# Initialisation de la hauteur et la largeur de l´écran  
W = 700
H = 600
size = [W, H]

ball_list=[]

def blitRotate(surf, image, pos, originPos, angle):

    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)
    # draw rectangle around the image
    pygame.draw.rect(surf, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()),2)
    
    
class Ball:
    """
    Classe pour définir les carctéristiques des balles.
    """
    def __init__(self,x,y):        
        self.speed_x = 0
        self.speed_y = 0
        self.color=(0,0,0)
        self.r=20
        self.x = x
        self.y = y

class Player:
    def __init__(self):
        self.x = W/2
        self.y = H/2
        self.image = pygame.image.load('assets/vaisseau.png')
        
def randcol():
    '''crée un tuple de trois valeurs comprises entre 0 et 255'''
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255)) 
 

def make_ball():
    """
    Crée une nouvelle balle
    """
    ball = Ball(100,100)
    
#     ball.x = random.randint(ball.r, W - ball.r)
#     ball.y = random.randint(ball.r, H - ball.r)
 
    ball.speed_x = random.randint(-4, 4)
    ball.speed_y = random.randint(-4, 4)
    
    ball.color=randcol()
    ball.r = random.randint(10,20)
 
    return ball

class Tir:
    """
    Classe pour définir les tirs.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed_x = 0
        self.speed_y = 0
        self.color=(0,0,0)
        self.r=2

def make_tir():
    """
    Crée un tir
    """
    tir = Tir()
    tir.x0 = 100
    tir.y0 = 100
    tir.x = 100
    tir.y = 100
 
    tir.speed_x = random.randint(-4, 4)
    tir.speed_y = random.randint(-4, 4)
    
    tir.color=BLACK
 
    return tir
     