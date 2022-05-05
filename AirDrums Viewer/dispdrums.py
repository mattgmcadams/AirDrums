# Imports
import os
import pygame
import sys
from pygame.locals import *

# Initializing
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen parameters
SCREEN_WIDTH = 983
SCREEN_HEIGHT = 553

# Hitbox Transparency
TRANS = 0

# Create a screen (16:9)
DISPLAYSURF = pygame.display.set_mode((983, 553))
pygame.display.set_caption("AirDrums Viewer")
background = pygame.image.load("drums.png")


# Classes
class Snare(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 100
        self.x = 195
        self.y = 390
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.image.fill(WHITE)
        self.image.set_alpha(TRANS)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.sound = pygame.mixer.Sound('SNARE.wav')

    def play(self):
        pygame.mixer.Sound.play(self.sound)


class HighTom(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 85
        self.x = 335
        self.y = 185
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.image.fill(WHITE)
        self.image.set_alpha(TRANS)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.sound = pygame.mixer.Sound('TOM1.wav')

    def play(self):
        pygame.mixer.Sound.play(self.sound)


class MedTom(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 90
        self.x = 620
        self.y = 190
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.image.fill(WHITE)
        self.image.set_alpha(TRANS)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.sound = pygame.mixer.Sound('TOM2.wav')

    def play(self):
        pygame.mixer.Sound.play(self.sound)


class LowTom(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 100
        self.x = 780
        self.y = 360
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.image.fill(WHITE)
        self.image.set_alpha(TRANS)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.sound = pygame.mixer.Sound('TOM3.wav')

    def play(self):
        pygame.mixer.Sound.play(self.sound)


class Floor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 50
        self.x = 475
        self.y = 320
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.image.fill(WHITE)
        self.image.set_alpha(TRANS)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.sound = pygame.mixer.Sound('FLOOR.wav')

    def play(self):
        pygame.mixer.Sound.play(self.sound)


class Crash(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 115
        self.x = 865
        self.y = 120
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.image.fill(WHITE)
        self.image.set_alpha(TRANS)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.sound = pygame.mixer.Sound('CRASH.wav')

    def play(self):
        pygame.mixer.Sound.play(self.sound)


class HHOpen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 90
        self.x = 100
        self.y = 115
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.image.fill(WHITE)
        self.image.set_alpha(TRANS)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.sound = pygame.mixer.Sound('HHOPEN.wav')

    def play(self):
        pygame.mixer.Sound.play(self.sound)


class HHClosed(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 90
        self.x = 100
        self.y = 115
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.image.fill(WHITE)
        self.image.set_alpha(TRANS)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.sound = pygame.mixer.Sound('HHCLOSED.wav')

    def play(self):
        pygame.mixer.Sound.play(self.sound)


class HHPedal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 20
        self.x = 225
        self.y = 250
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.image.fill(WHITE)
        self.image.set_alpha(TRANS)
        self.rect = self.image.get_rect(center=(self.x, self.y))


# Setting Up Sprites
S1 = Snare()
T1 = HighTom()
T2 = MedTom()
T3 = LowTom()
B1 = Floor()
S2 = Crash()
H0 = HHOpen()
H1 = HHClosed()
P1 = HHPedal()
# Creating Sprite Groups
drums = pygame.sprite.Group()
drums.add(S1, S2, H0, T1, T2, T3, B1)
pedal = pygame.sprite.Group()
pedal.add(P1)
pedal.draw(DISPLAYSURF)
# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if P1.rect.collidepoint(event.pos):
                if H0 in drums:
                    H0.kill()
                    drums.add(H1)
                else:
                    H1.kill()
                    drums.add(H0)
            for drum in drums:
                if drum.rect.collidepoint(event.pos):  # event.pos is the mouse position.
                    drum.play()
    # Draw background
    DISPLAYSURF.blit(background, (0, 0))
    # Moves and Re-draws all Sprites
    drums.draw(DISPLAYSURF)
    pygame.display.update()
    FramePerSec.tick(FPS)
