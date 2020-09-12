# Functioning clock on Python usng pygame and a self created library, set the weekday, hour and minute, and let it run

import pygame
from pygametexting import pyg_text
import time

def set_time(time_list,sett_list,v):
    time_list[v] = input(sett_list[v][0])
    try:
        time_list[v] = int(time_list[v])
        while not (sett_list[v][1]<=time_list[v]<sett_list[v][2]):
            print("Invalid value. Try again...")
            set_time(time_list,sett_list,v)
    except:
        print("Invalid input type. Try again...")
        set_time(time_list,sett_list,v)

pygame.init()

win=pygame.display.set_mode((500,500))

pygtxt=pyg_text(20,(255,255,255),"comicsansms",win)

black = (0,0,0)

idhm = ["","",""]

sett = [["day? ", 1, 8, 7], ["hrs? ", 0, 24, 24], ["min? ", 0, 60, 60]]

semana = ["Dom","Seg","Ter","Qua","Qui","Sex","Sab"]

for u in range(len(idhm)):
    while type(idhm[u])!=int:
        set_time(idhm,sett,u)

now = time.time()

idhm[0] = idhm[0]-1
cdhm = [idhm[0], idhm[1], idhm[2]]
rdhm = [0,0,0]
fdhms = [0,0,0,0]


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    win.fill(black)
    
    tw = time.time() - now
    
    fdhms[3] = int(tw%60)
    
    rdhm[2] = tw/60
    
    rdhm[1] = (idhm[2]*60+tw)/60
    rdhm[1] = rdhm[1]/60
    
    rdhm[0] = (idhm[1]*(60**2)+idhm[2]*60+tw)/60
    rdhm[0] = rdhm[0]/60
    rdhm[0] = rdhm[0]/24
    
    fdhms[2] = int(cdhm[2] + rdhm[2])
    fdhms[1] = int(cdhm[1] + rdhm[1])
    fdhms[0] = int(cdhm[0] + rdhm[0])
    
    for i in range(len(cdhm)):
        if fdhms[i] == sett[i][3]:
            cdhm[i] -= sett[i][3]
            fdhms[i] = int(cdhm[i] + rdhm[i])
    
    cur_time = "{0} - {1:0>2}:{2:0>2}:{3:0>2}".format(semana[fdhms[0]],fdhms[1],fdhms[2],fdhms[3])
            
    pygtxt.screen_text_centerpos(cur_time,250,250)
        
    pygame.display.update()
    
pygame.quit()
