import pygame

#initializing pygame
pygame.init()
clock=pygame.time.Clock()

#Screen setup
screen_width=700
screen_height=400
screen=pygame.display.set_mode((screen_width,screen_height))

#colors
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

#Images
color_img=pygame.image.load("assets/n.jpg").convert_alpha()
background_img=pygame.image.load("assets/environment.png").convert_alpha()
background_img.set_alpha(100)
platform_img=pygame.image.load("assets/platform.png") 
key_img=pygame.image.load("assets/key.png") 
door_open_img=pygame.image.load("assets/doorOpen.png") 
door_close_img=pygame.image.load("assets/doorClose.png") 
win_img=pygame.image.load("assets/winScreen.png") 
ground_img=pygame.image.load("assets/ground.png").convert_alpha()
cloud=pygame.image.load("assets/cloud.png")
player_img1=pygame.image.load("assets/joe0.png") 
player_img2=pygame.image.load("assets/joe1.png") 
player_img3=pygame.image.load("assets/joe2.png") 
player_img4=pygame.image.load("assets/joe3.png") 
player_img5=pygame.image.load("assets/joe4.png") 
cloud.set_alpha(200)
player_jump=pygame.image.load("assets/joe0.png")
keys_text_img=pygame.image.load("assets/keysText.png")
spikes_img = pygame.image.load("assets/dragon_left.png").convert_alpha()
spikes_img2 = pygame.image.load("assets/dragon_right.png").convert_alpha()

playerImgHeight=50
playerImgWidth=30
doorHeight=100
doorWidth=100
#Image Scaling
background_img = pygame.transform.scale(background_img, (screen_width, screen_height-100))
color_img = pygame.transform.scale(color_img, (screen_width, screen_height))
player_jump_right = pygame.transform.scale(player_jump, (playerImgWidth, playerImgHeight))
player_jump_left = pygame.transform.scale(pygame.transform.flip(player_jump,True,False), (playerImgWidth, playerImgHeight))
door_close_img=pygame.transform.smoothscale(door_close_img,(100,100))
door_open_img=pygame.transform.smoothscale(door_open_img,(100,100))
keys_text_img=pygame.transform.smoothscale(keys_text_img,(100,50))
key_img=pygame.transform.smoothscale(key_img,(30,20))
cloud = pygame.transform.scale(cloud, (100, 50))
platform_img150 = pygame.transform.scale(platform_img, (150, 20))
platform_img100 = pygame.transform.scale(platform_img, (100, 20))
platform_img50 = pygame.transform.scale(platform_img, (50, 20))
spikes_img = pygame.transform.scale(spikes_img, (50, 50))
spikes_img2 = pygame.transform.scale(spikes_img2, (50, 50))
door_img=door_close_img

player_img_list_right = [pygame.transform.scale(player_img1, (playerImgWidth, playerImgHeight)),
                         pygame.transform.scale(player_img2, (playerImgWidth, playerImgHeight)),
                         pygame.transform.scale(player_img3, (playerImgWidth, playerImgHeight)),
                         pygame.transform.scale(player_img4, (playerImgWidth, playerImgHeight)),
                         pygame.transform.scale(player_img5, (playerImgWidth, playerImgHeight))]

player_img_list_left = [pygame.transform.scale(pygame.transform.flip(player_img1,True,False), (playerImgWidth, playerImgHeight)),
                        pygame.transform.scale(pygame.transform.flip(player_img2,True,False), (playerImgWidth, playerImgHeight)),
                        pygame.transform.scale(pygame.transform.flip(player_img3,True,False), (playerImgWidth, playerImgHeight)),
                        pygame.transform.scale(pygame.transform.flip(player_img4,True,False), (playerImgWidth, playerImgHeight)),
                        pygame.transform.scale(pygame.transform.flip(player_img5,True,False), (playerImgWidth, playerImgHeight))]

player_img = player_img_list_right

#characters
player=pygame.Rect(100,screen_height-145,playerImgWidth,playerImgHeight)
ground=pygame.Rect(0,screen_height-90,screen_width,40)
ground_img = pygame.transform.scale(ground_img, (screen_width, 90))
door=pygame.Rect(screen_width-100,0,doorWidth,doorHeight)
platform1 = pygame.Rect(screen_width-150,doorHeight, 150, 5)
platform2 = pygame.Rect(0, 200, 100, 5)
platform3 = pygame.Rect(150, 250, 50, 5)
platform4 = pygame.Rect(300, 200, 100, 5)
platform5 = pygame.Rect(450, 150, 50, 5)
spikes=pygame.Rect(250,screen_height-135,50,50)
spikes2=pygame.Rect(400,screen_height-135,50,50)
bananas=[]
remainingTime=10

velX=0
velY=0

isMoving=False
value=0

key_count=0

#new events
REDUCETIME= pygame.USEREVENT + 2
pygame.time.set_timer(REDUCETIME, 500)

#font
score_font=pygame.font.Font('freesansbold.ttf', 16)
over_font=pygame.font.Font('freesansbold.ttf', 25)


##############create keys#################template code
gameState='play'

keys = [pygame.Rect(platform2.x,platform2.y-25,40,50),
        pygame.Rect(screen_width/2,ground.y-25,40,50),
        pygame.Rect(platform4.x,platform4.y-25,40,50),]
#####################################

cloud1X = 50
cloud2X = 300
cloud3X = 550
spike_x = 5

#Game Loop
while True:
    screen.blit(color_img, (0, 0))
    screen.blit(background_img, (0, 100))
    screen.blit(ground_img, (0, screen_height-90))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velX=-5
                player_img=player_img_list_left
                isMoving=True
            if event.key ==pygame.K_RIGHT:
                velX=5
                player_img=player_img_list_right
                isMoving=True
            if event.key ==pygame.K_SPACE:
                velY=-12
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                velX=0
                isMoving=False
            if event.key ==pygame.K_RIGHT:
                velX=0
                isMoving=False
            if event.key ==pygame.K_SPACE:
                pass
        if event.type==REDUCETIME:
            remainingTime-=1
    if isMoving:
       value += 1
    if value >= len(player_img): 
        value =0 
    playerImg=player_img[value]
    
    #moveplayer
    player.x+=velX
    player.y+=velY
    
    #gravity
    velY+=1
    
    #collision with ground
    if player.colliderect(ground.x,ground.y-velY,ground.width,ground.height):
        velY=0  
    else:
        if(velX<0):
          playerImg=player_jump_left
        else:
          playerImg=player_jump_right
        
    for i in keys:
        screen.blit(key_img,i)
        if player.colliderect(i):
            key_count+=1
            keys.remove(i)    

###############################################################################
    if key_count==3:
        door_img=door_open_img
        if(player.colliderect(door)):
            win_text=over_font.render("Winner!", False, (255,0,0))   
            screen.blit(win_img,[220,100]) 
            playerImgHeight=int(playerImgHeight*0.99)
            playerImgWidth=int(playerImgWidth*0.99)
            playerImg=pygame.transform.scale(playerImg,(playerImgWidth,playerImgHeight) )
            player.x=door.centerx
            player.midbottom=door.midbottom
    

    if platform1.colliderect(player):
        velY = 0
    elif platform2.colliderect(player):
        velY = 0
    elif platform3.colliderect(player):
        velY = 0
    elif platform4.colliderect(player):
        velY = 0
    elif platform5.colliderect(player):
        velY = 0

    if(player.colliderect(spikes)):
        win_text=over_font.render("YOU LOST!", False, (255,0,0))
        pygame.quit()
        break

    if (spikes.colliderect(spikes2)):
        spikes_img = pygame.transform.flip(spikes_img,True,False)
        spikes_img2 = pygame.transform.flip(spikes_img2,True,False)
        spike_x = 5

    screen.blit(keys_text_img,[15,15])
###############################################################################

    score_text=score_font.render(str(key_count)+" / 3", False, (255,255,255))   
    screen.blit(score_text,[75,30])     

    #display characters
    #pygame.draw.rect(screen,RED, player)
    #pygame.draw.rect(screen,GREEN, door)
    
    screen.blit(cloud, (cloud1X, 50))
    if cloud1X < -100:
        cloud1X = screen_width
    else:
        cloud1X -= 2

    screen.blit(cloud, (cloud2X, 75))
    if cloud2X < -50:
        cloud2X = screen_width
    else:
        cloud2X -= 1

    screen.blit(cloud, (cloud3X, 100))
    if cloud3X < 0:
        cloud3X = screen_width
    else:
        cloud3X -= 2

    if spikes.x < 0 or spikes2.x > screen_width:
        spikes_img = pygame.transform.flip(spikes_img,True,False)
        spikes_img2 = pygame.transform.flip(spikes_img2,True,False)
        spike_x = -5
    
    spikes.x -= spike_x
    spikes2.x += spike_x


    screen.blit(door_img,door)
    screen.blit(playerImg,player)
    screen.blit(spikes_img,spikes)
    screen.blit(spikes_img2,spikes2)   
    screen.blit(platform_img50,platform3)
    screen.blit(platform_img50,platform5)
    screen.blit(platform_img100,platform2)
    screen.blit(platform_img100,platform4)
    screen.blit(platform_img150,platform1)
    
    pygame.display.update()
    clock.tick(30)