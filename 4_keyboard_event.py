import pygame
pygame.init()

screen_width = 480 
screen_height = 640 
screen = pygame.display.set_mode((screen_width, screen_height)) 

pygame.display.set_caption("Nado Game") 

background = pygame.image.load("C:/DevPy/PyGameEx/background.png")
charactor = pygame.image.load("C:/DevPy/PyGameEx/charactor.png") 
charactor_size = charactor.get_rect().size 
charactor_width = charactor_size[0] 
charactor_height = charactor_size[1] 
charactor_x_pos = (screen_width - charactor_width) / 2 
charactor_y_pos = screen_height - charactor_height 

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False; 
            
    screen.blit(background, (0, 0)) 
    screen.blit(charactor, (charactor_x_pos, charactor_y_pos))  
    pygame.display.update() 
         
pygame.quit() 