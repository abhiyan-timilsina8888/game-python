import pygame
import sys
import random
#pygamelai.initialize garxa
pygame.init()

#game ko size halney
screen_width= 800
screen_height=400
ground_height=50
white =(255,255,255)

#aaba size haru lai jodney i.e game ko window banaune
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("run as much as you can!")
  
  
#now add (player character, image, obstacles, background etc)
player_image=pygame.image.load("player.png")
obstacle_image=pygame.image.load("obstacle.png")
background_image=pygame.image.load("background.png")

#now adding dimensions to the charcater and obstacles
player_width , player_height =player_image.get_size()
obstacle_width , obstacle_height = obstacle_image.get_size()

#adding or inputing the position of player
player_x = 100
player_y= screen_height - ground_height - player_height
player_speed = 10
 
#making list for obstacles
obstacles = []

score=0
font=pygame.font.font(None,36)

#game loop
running= True
for event  in pygame.event.get():
    if event.type ==pygame.quit:
        running= False
        
        
#move player
keys=pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
        player_x -= player_speed
if keys[pygame.K_RIGHT]:
        player_x += player_speed
        
#generates the obstacles
if random.randint(1,100)<3:
    obstacle_x=screen_width
    obstacles_y = screen_height - ground_height - obstacle_height
    obstacles.append([obstacle_x,obstacles_y])
    
#updating obsatcle postion    
for obstacle in obstacles :
    obstacle[0] -= player_speed
    
# removing the obsatcle bigger then screen size
obstacles=[obstacle for obstacle in obstacles if obstacle[0] > -screen_width]

# check for collision
for obsctacle in obstacles:
    if(
        player_x < obstacle[0] + obstacle_width
        and player_x +player_width> obstacle[0]
        and player_y <obstacle[1] + obstacle_height
        and player_y +player_height >obstacle[1]
    ):
        running= False
        
# update score     
score += 1 

#clear the screen
screen.fill(white)

#draw a background image
screen.blit(background_image,(0,0))

#draw a player character
screen.blit(player_image,(player_x,player_y))

#draw obstacles
for obsctacle in obstacles:
    screen.blit(obstacle_image,(obsctacle[0],obsctacle[1]))
    
# display score
text =font.render("score: "+str(score),True,(0,0,0))
text.blit(text,(10,10))

#update the screen
pygame.display.flip()

#exit pygame
pygame.quit()
sys.exit()

            
    
        


