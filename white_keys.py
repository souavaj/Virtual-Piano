import piano_list as pl
import pygame

width = 26 * 35
height = 400
screen = pygame.display.set_mode([width, height])

def draw_key_a():
    for i, key in enumerate(pl.white_keys):
        if key == 'C2' and pygame.K_a:
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_b():
    for i, key in enumerate(pl.white_keys):
        if key == 'D2':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_c():
    for i, key in enumerate(pl.white_keys):
        if key == 'E2':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
            
def draw_key_d():
    for i, key in enumerate(pl.white_keys):
        if key == 'F2':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_e():
    for i, key in enumerate(pl.white_keys):
        if key == 'G2':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)

def draw_key_f():
    for i, key in enumerate(pl.white_keys):
        if key == 'A2':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_g():
    for i, key in enumerate(pl.white_keys):
        if key == 'B2':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_h():
    for i, key in enumerate(pl.white_keys):
        if key == 'C3':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_i():
    for i, key in enumerate(pl.white_keys):
        if key == 'D3':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_j():
    for i, key in enumerate(pl.white_keys):
        if key == 'E3':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_k():
    for i, key in enumerate(pl.white_keys):
        if key == 'F3':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_l():
    for i, key in enumerate(pl.white_keys):
        if key == 'G3':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_m():
    for i, key in enumerate(pl.white_keys):
        if key == 'A3':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_n():
    for i, key in enumerate(pl.white_keys):
        if key == 'B3':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_o():
    for i, key in enumerate(pl.white_keys):
        if key == 'C4':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_p():
    for i, key in enumerate(pl.white_keys):
        if key == 'D4':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_q():
    for i, key in enumerate(pl.white_keys):
        if key == 'E4':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_r():
    for i, key in enumerate(pl.white_keys):
        if key == 'F4':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_s():
    for i, key in enumerate(pl.white_keys):
        if key == 'G4':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_t():
    for i, key in enumerate(pl.white_keys):
        if key == 'A4':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_u():
    for i, key in enumerate(pl.white_keys):
        if key == 'B4':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_v():
    for i, key in enumerate(pl.white_keys):
        if key == 'C5':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_w():
    for i, key in enumerate(pl.white_keys):
        if key == 'D5':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_x():
    for i, key in enumerate(pl.white_keys):
        if key == 'E5':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_y():
    for i, key in enumerate(pl.white_keys):
        if key == 'F5':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)
        
def draw_key_z():
    for i, key in enumerate(pl.white_keys):
        if key == 'G5':
            pygame.draw.rect(screen, 'red', [i * 35, height - 100, 35, 100], 2, 2)

