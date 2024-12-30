# Import packages to use
import tkinter as tk
import pygame
import mido
from pynput.keyboard import Key, Controller
import piano_list as pl
import white_keys as dk
import black_keys as db


#Initiate pygame package
pygame.init()
pygame.mixer.set_num_channels(44)

#Define variables to adjust virtual piano
small_font = pygame.font.Font(None, 16)
fps = 60
timer = pygame.time.Clock()
width = 26 * 35
height = 400
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("My Virtual Piano")

active_white = [] #Save white rect as active
active_black = [] #Save black rect as active

#Define function to draw 44 keys of a piano
def draw_piano(whites, blacks):
    #Create white keys
    white_rects = []
    for i in range(len(pl.white_keys)):
        rect = pygame.draw.rect(screen, 'white', [i * 35, height - 300, 35, 300], 0, 2)
        white_rects.append(rect)
        pygame.draw.rect(screen, 'black', [i * 35, height - 300, 35, 300], 2, 2)
        key_label = small_font.render(pl.white_keys[i], True, 'black')
        screen.blit(key_label, (i * 35 + 10, height - 20))
    skip_count = 0
    last_skip = 0
    skip_track = 0
    
    #Create black keys
    black_rects = []
    for i in range(len(pl.black_keys)):
        rect = pygame.draw.rect(screen, 'black', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 0, 2)
        for j in range(len(blacks)):
            if blacks[j][0] == i:
                if blacks[j][1] > 0:
                    pygame.draw.rect(screen, 'green', [23 + (i * 35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
                    blacks[j][1] -= 1
        key_label = small_font.render(pl.black_keys[i], True, 'white')
        screen.blit(key_label, (25 + (i *35) + (skip_count * 35), height - 120))
        black_rects.append(rect)
        
        #Create space between black keys
        skip_track += 1
        if last_skip != 2 and skip_track == 3: 
            last_skip = 2
            skip_track = 0
            skip_count += 1
        elif last_skip != 3 and skip_track == 2:
            last_skip = 3
            skip_track = 0
            skip_count += 1            
            
    return white_rects, black_rects, whites, blacks


#Create mapping dictionary
key_mapping = {'C2': 'a', 'D2': 'b', 'E2': 'c', 'F2': 'd', 'G2': 'e', 'A2': 'f', 'B2': 'g', 'C3': 'h', 'D3': 'i', 'E3': 'j', 'F3': 'k', 'G3': 'l', 'A3': 'm', 'B3': 'n', 'C4': 'o', 'D4': 'p', 'E4': 'q', 'F4': 'r', 'G4': 's', 'A4': 't', 'B4': 'u', 'C5': 'v', 'D5': 'w', 'E5': 'x', 
'F5': 'y', 'G5': 'z', 'C#2': 'F1', 'D#2': 'F2', 'F#2': 'F3', 'G#2': 'F4', 'A#2': 'F5', 'C#3': 'F6', 'D#3': 'F7', 'F#3': 'F8', 'G#3': '1', 'A#3': '2', 'C#4': '3', 'D#4': '4', 'F#4': '5', 'G#4': '6', 'A#4': '7', 'C#5': '8', 'D#5': '9', 'F#5': '0'}

#def midi_to_keyboard():
 #   midi_file = input('MIDI File Location: ')
  #  mid = mido.MidiFile(midi_file)
   # keyboard = Controller()

    #for msg in mid.tracks[0]:
     #   if msg.type == 'note_on':
      #      note_value = msg.note
       #     key_press = key_mapping.get(note_value, None)

        #    if key_press:
         #       keyboard.press(key_press)
        #elif msg.type == 'note_off':
         #   note_value = msg.note
          #  key_press = key_mapping.get(note_value, None)
           # if key_press:
            #    keyboard.release(key_press)
    
    #print(midi_file)

#window = tk.Tk()
#window.title('MIDI Music Sheet File')

#button = tk.Button(window, text='Click Here First: ', command=lambda: midi_to_keyboard(), anchor='center', bg='lightgray', width=15, height=5)
#button.pack()

#window.mainloop()

# Run the program
start_time = 0
run = True
while run:
    timer.tick(fps)
    screen.fill('gray')
    white_keys, black_keys, active_white, active_black = draw_piano(active_white, active_black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            #Activate white keys
            if event.key == pygame.K_a:
                key_a = pygame.mixer.Sound("D:\IT_Courses\IT_697-IoT\music_sound\C2.wav")
                key_a.play()
                if key_a.play():
                    dk.draw_key_a()
            if event.key == pygame.K_b:
                key_b = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\D2.wav')
                key_b.play()
                if key_b.play():
                    dk.draw_key_b()
            if event.key == pygame.K_c:
                key_c = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\E2.wav')
                key_c.play()
                if key_c.play():
                    dk.draw_key_c()
            if event.key == pygame.K_d:
                key_d = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\F2.wav')
                key_d.play()
                if key_d.play():
                    dk.draw_key_d()
            if event.key == pygame.K_e:
                key_e = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\G2.wav')
                key_e.play()
                if key_e.play():
                    dk.draw_key_e()
            if event.key == pygame.K_f:
                key_f = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\A2.wav')
                key_f.play()
                if key_f.play():
                    dk.draw_key_f()
            if event.key == pygame.K_g:
                key_g = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\B2.wav')
                key_g.play()
                if key_g.play():
                    dk.draw_key_g()
            if event.key == pygame.K_h:
                key_h = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\C3.wav')
                key_h.play()
                if key_h.play():
                    dk.draw_key_h()
            if event.key == pygame.K_i:
                key_i = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\D3.wav')
                key_i.play()
                if key_i.play():
                    dk.draw_key_i()
            if event.key == pygame.K_j:
                key_j = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\E3.wav')
                key_j.play()
                if key_j.play():
                    dk.draw_key_j()
            if event.key == pygame.K_k:
                key_k = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\F3.wav')
                key_k.play()
                if key_k.play():
                    dk.draw_key_k()
            if event.key == pygame.K_l:
                key_l = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\G3.wav')
                key_l.play()
                if key_l.play():
                    dk.draw_key_l()
            if event.key == pygame.K_m:
                key_m = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\A3.wav')
                key_m.play()
                if key_m.play():
                    dk.draw_key_m()
            if event.key == pygame.K_n:
                key_n = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\B3.wav')
                key_n.play()
                if key_n.play():
                    dk.draw_key_n()
            if event.key == pygame.K_o:
                key_o = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\C4.wav')
                key_o.play()
                if key_o.play():
                    dk.draw_key_o()
            if event.key == pygame.K_p:
                key_p = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\D4.wav')
                key_p.play()
                if key_p.play():
                    dk.draw_key_p()
            if event.key == pygame.K_q:
                key_q = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\E4.wav')
                key_q.play()
                if key_q.play():
                    dk.draw_key_q()
            if event.key == pygame.K_r:
                key_r = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\F4.wav')
                key_r.play()
                if key_r.play():
                    dk.draw_key_r()
            if event.key == pygame.K_s:
                key_s = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\G4.wav')
                key_s.play()
                if key_s.play():
                    dk.draw_key_s()
            if event.key == pygame.K_t:
                key_t = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\A4.wav')
                key_t.play()
                if key_t.play():
                    dk.draw_key_s()
            if event.key == pygame.K_u:
                key_u = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\B4.wav')
                key_u.play()
                if key_u.play():
                    dk.draw_key_u()
            if event.key == pygame.K_v:
                key_v = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\C5.wav')
                key_v.play()
                if key_v.play():
                    dk.draw_key_v()
            if event.key == pygame.K_w:
                key_w = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\D5.wav')
                key_w.play()
                if key_w.play():
                    dk.draw_key_w()
            if event.key == pygame.K_x:
                key_x = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\E5.wav')
                key_x.play()
                if key_x.play():
                    dk.draw_key_x()
            if event.key == pygame.K_y:
                key_y = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\F5.wav')
                key_y.play()
                if key_y.play():
                    dk.draw_key_y()
            if event.key == pygame.K_z:
                key_z = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\G5.wav')
                key_z.play()
                if key_z.play():
                    dk.draw_key_z()
            
            #Activate black keys
            if event.key == pygame.K_F1:
                key_f1 = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\C#2.wav')
                key_f1.play()
                if key_f1.play():
                    db.draw_key_f1()
            if event.key == pygame.K_F2:
                key_f2 = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\D#2.wav')
                key_f2.play()
                if key_f2.play():
                    db.draw_key_f2()
            if event.key == pygame.K_F3:
                key_f3 = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\F#2.wav')
                key_f3.play()
                if key_f3.play():
                    db.draw_key_f3()
            if event.key == pygame.K_F4:
                key_f4 = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\G#2.wav')
                key_f4.play()
                if key_f4.play():
                    db.draw_key_f4()
            if event.key == pygame.K_F5:
                key_f5 = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\A#2.wav')
                key_f5.play()
                if key_f5.play():
                    db.draw_key_f5()
            if event.key == pygame.K_F6:
                key_f6 = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\C#3.wav')
                key_f6.play()
                if key_f6.play():
                    db.draw_key_f6()
            if event.key == pygame.K_F7:
                key_f7 = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\D#3.wav')
                key_f7.play()
                if key_f7.play():
                    db.draw_key_f7()
            if event.key == pygame.K_F8:
                key_f8 = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\F#3.wav')
                key_f8.play()
                if key_f8.play():
                    db.draw_key_f8()
            if event.key == pygame.K_1:
                key_1 = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\G#3.wav')
                key_1.play()
                if key_1.play():
                    db.draw_key_1()
            if event.key == pygame.K_2:
                key_2 = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\A#3.wav')
                key_2.play()
                if key_2.play():
                    db.draw_key_2()
            if event.key == pygame.K_3:
                key_3 = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\C#4.wav')
                key_3.play()
                if key_3.play():
                    db.draw_key_3()
            if event.key == pygame.K_4:
                key_4 = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\D#4.wav')
                key_4.play()
                if key_4.play():
                    db.draw_key_4()
            if event.key == pygame.K_5:
                key_5 = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\F#4.wav')
                key_5.play()
                if key_5.play():
                    db.draw_key_5()
            if event.key == pygame.K_6:
                key_6 = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\G#4.wav')
                key_6.play()
                if key_6.play():
                    db.draw_key_6()
            if event.key == pygame.K_7:
                key_7 = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\A#4.wav')
                key_7.play()
                if key_7.play():
                    db.draw_key_7()
            if event.key == pygame.K_8:
                key_8 = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\C#5.wav')
                key_8.play()
                if key_8.play():
                    db.draw_key_8()
            if event.key == pygame.K_9:
                key_9 = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\D#5.wav')
                key_9.play()
                if key_9.play():
                    db.draw_key_9()
            if event.key == pygame.K_0:
                key_0 = pygame.mixer.Sound('D:\IT_Courses\IT_697-IoT\music_sound\F#5.wav')
                key_0.play()
                if key_0.play():
                    db.draw_key_0()
            
    pygame.display.flip()
pygame.quit()
