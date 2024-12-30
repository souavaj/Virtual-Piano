import piano_list as pl
import pygame

width = 26 * 35
height = 400
screen = pygame.display.set_mode([width, height])
black_pos = [(1.5, 0), (2.5, 0), (4.5, 0), (5.5, 0), (6.5, 0)]
skip_count = 0

def draw_key_f1():
    for i, key in enumerate(pl.black_keys):
        if key == 'C#2' and pygame.K_F1:
            pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
        
def draw_key_f2():
    for i, key in enumerate(pl.black_keys):
        if key == 'D#2':
            pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
        
def draw_key_f3():
    for i, key in enumerate(pl.black_keys):
        if i:
            i += 1
        if key == 'F#2':
            pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
     
def draw_key_f4():
    for i, key in enumerate(pl.black_keys):
        if i:
            i += 1
        if key == 'G#2':
            pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
        
def draw_key_f5():
    for i, key in enumerate(pl.black_keys):
        if i:
            i += 1
        if key == 'A#2':
            pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)

def draw_key_f6():
    for i, key in enumerate(pl.black_keys):
        if i:
            i += 2
        if key == 'C#3':
            pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
        
def draw_key_f7():
    for i, key in enumerate(pl.black_keys):
        if i:
            i += 2
        if key == 'D#3':
            pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
        
def draw_key_f8():
    for i, key in enumerate(pl.black_keys):
        if i:
            i += 3
        if key == 'F#3':
            pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
        
def draw_key_1():
    for i, key in enumerate(pl.black_keys):
        if i:
            i += 3
        if key == 'G#3':
            pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
        
def draw_key_2():
    for i, key in enumerate(pl.black_keys):
        if i:
            i += 3
        if key == 'A#3':
            pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
        
def draw_key_3():
    for i, key in enumerate(pl.black_keys):
        if i:
            i += 4
        if key == 'C#4':
            pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
        
def draw_key_4():
    for i, key in enumerate(pl.black_keys):
        if i:
            i += 4
        if key == 'D#4':
           pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
        
def draw_key_5():
    for i, key in enumerate(pl.black_keys):
        if i:
            i += 5
        if key == 'F#4':
            pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
        
def draw_key_6():
    for i, key in enumerate(pl.black_keys):
        if i:
            i += 5
        if key == 'G#4':
            pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
        
def draw_key_7():
    for i, key in enumerate(pl.black_keys):
        if i:
            i += 5
        if key == 'A#4':
            pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
        
def draw_key_8():
    for i, key in enumerate(pl.black_keys):
        if i:
            i += 6
        if key == 'C#5':
            pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
        
def draw_key_9():
    for i, key in enumerate(pl.black_keys):
        if i:
            i += 6
        if key == 'D#5':
            pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
        
def draw_key_0():
    for i, key in enumerate(pl.black_keys):
        if i:
            i += 7
        if key == 'F#5':
            pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
