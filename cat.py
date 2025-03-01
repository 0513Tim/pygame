import pygame, sys
from pygame.locals import *

# 初始化
pygame.init()
FPS = 10 # 設定每秒幾禎
Clock = pygame.time.Clock() # Clock

# 設定視窗
DISPLAYSURF = pygame.display.set_mode((800,600), pygame.RESIZABLE, 32)
pygame.display.set_caption('Cat ')

# 設定一些基本的數值
black = (0, 0, 0)
catImg = pygame.image.load('cat.png')
catImg = pygame.transform.scale(catImg, (200, 200))  # 調整圖片大小為 50x50
font = pygame.font.SysFont("Microsoft JhengHei", 24)
# 設定貓的 x y 軸
catx = 100
caty = 100
direction = 'right' # 一開始的方向

while True: # the main game loop
    DISPLAYSURF.fill(black)

    if direction == 'right': # 往右跑
        catx = catx + 5 
        
        if catx > DISPLAYSURF.get_width()-catImg.get_width(): # 如果跑到邊界 就讓貓往下跑
            direction = 'left'

    elif direction == 'left': # 往左跑
        catx = catx - 5
        if catx < 10: 
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty)) #繪製覆蓋整個視窗

    # 偵測事件
    for event in pygame.event.get():
        # 按叉叉就退出
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #記得更新畫面
    DISPLAYSURF.blit(font.render(str(Clock.get_fps()), True, (255, 255, 255)), (10, 10))
    print(Clock.get_fps())
    
    pygame.display.update()
    Clock.tick(FPS)
