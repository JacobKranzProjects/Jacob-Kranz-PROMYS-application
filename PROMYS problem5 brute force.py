import math
import pygame
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (10,50)



def simplify(a, b):
    d = math.gcd(a, b)
    return (int(a/d), int(b/d))
    return a, b

def removeduplicates(list):
    res = []
    [res.append(x) for x in list if x not in res]
    return res
    

def rule2(list):
    returnlist = []
    for frac in list:
        if simplify(frac[1], frac[0]*2) not in list:
            returnlist.append(simplify(frac[1], frac[0]*2))
    return removeduplicates(returnlist)



def rule3(list, adds, a):
    additions = []
    returnlist = []
    for x in adds:
        additions.append(x)
    for x in list:
        additions.append(x)
    

    for ab in additions:
        for cd in adds:
            if ab != cd and (ab[0]+cd[0])<a and (ab[1]+cd[1])<a:
                returnlist.append(simplify(ab[0]+cd[0], ab[1]+cd[1]))
    
    
    return removeduplicates(returnlist)






list = [(1, 1)]
plist = []
pslist = ''


pygame.init()



win_size = (300, 400)
window = pygame.display.set_mode(win_size, pygame.RESIZABLE)
click = True
b=0
a = 175
while True:
    if b < 2:
        b = int(input("iterations"))
    b-=1
    pygame.draw.line(window, (255, 255, 0), (1, 2), (a, 2*a))
    pygame.draw.line(window, (255, 255, 0), (0, 0), (a, a))
    
    if click == True:
        additions = rule2(list)
        for x in rule3(list, additions, a):
            list.append(x)
        for x in additions:
            list.append(x)
        list = removeduplicates(list)
        
        for pt in list:
            window.fill((255, 255, 255), ((pt[0], pt[1]), (1, 1)))
        # click = False

        


    events = pygame.event.get()
    pygame.display.flip()
    for event in events:
        if event.type == pygame.QUIT:
            for frac in list:
                plist.append(frac)
                if len(plist) > 6:
                    pslist = str(plist)
                    pslist.replace('[', '').replace(']', '')
                    print(pslist)
                    pslist = ''
                    plist = []
            quit()

        if event.type == pygame.MOUSEBUTTONUP:
            click = True
            a+=10
        
    

