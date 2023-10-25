from pygame import *
from random import *
font.init()
#pygame.init()
window=display.set_mode((320,620))
display.set_caption('не смеяться')
window_width=700
color=(90,250,60)
'''rectx,recty=150,150
rectan=Rect(rectx,recty,width,height)'''
window.fill((0,0,0))
Font1=font.Font(None,30)
nosleep=True
rrect = Rect(0,0,100,100)
rect_color = (0,40,255)
draw.rect(window,rect_color,rrect)
show=True
def addinfo():
    info=''
    while event.key!=K_RETURN:
        info+=event.unicode
while show:
    for e in event.get():
        if e.type == QUIT:
            show=False
    display.update()
