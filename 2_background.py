import pygame
pygame.init()

screen_width = 480 
screen_height = 640 
screen = pygame.display.set_mode((screen_width, screen_height)) 

pygame.display.set_caption("Nado Game") 

background = pygame.image.load("C:/DevPy/PyGameEx/background.png")

running = True 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False; 
            
    screen.blit(background, (0, 0)) 
    # screen.fill((0, 0, 255)) 
    pygame.display.update() 
         
pygame.quit() 