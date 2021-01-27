import pygame


#-----------FROG-------------#
class Frog(pygame.sprite.Sprite):
    # Define constant values
    IMAGE = pygame.image.load('frog.png')
    STARTING_POSITION = (290, 480)
    SIZE = (20, 10)
    MOVE_DIST = 20
    lives = 3
    
    # Creates a Frog object
    def __init__(self):
        # Sprite Information
        super().__init__()
        self.image = Frog.IMAGE
        
        # Frog Information
        self.rect = pygame.Rect((0, 0), Frog.SIZE)
        self.rect.center = Frog.STARTING_POSITION

    # Key movement
    def move_left(self):
        if self.rect.centerx >= self.MOVE_DIST:
            self.rect.centerx -= self.MOVE_DIST
    
    def move_right(self):
        if self.rect.centerx <= 550:
            self.rect.centerx += self.MOVE_DIST
    
    def move_down(self):
        if self.rect.centery <= 460:
            self.rect.centery += self.MOVE_DIST
    
    def move_up(self):
        if self.rect.centery >= 20:
            self.rect.centery -= self.MOVE_DIST

    # When frog collides
    def collision(self):
        self.rect = pygame.Rect((0, 0), Frog.SIZE)
        self.rect.center = Frog.STARTING_POSITION
        self.lives -= 1
            

#-----------Log-------------#
class Log(pygame.sprite.Sprite):
    IMAGE = pygame.image.load('log.png')
    STARTING_POSITION = (400, 100)
    SIZE = (60, 30)
    MOVE_DIST = 2

    def __init__(self):
        super().__init__()
        self.image = Log.IMAGE

        self.rect = pygame.Rect((0,0), Log.SIZE)
        self.rect.center = Log.STARTING_POSITION

    def move_left(self):
        self.rect.centerx -= Log.MOVE_DIST
        if self.rect.centerx <= 0:
            self.rect.centerx = 600

    def move_right(self):
        self.rect.centerx += Log.MOVE_DIST
        if self.rect.centerx >= 600:
            self.rect.centerx = 0

            
#-----------Bus-------------#
class Bus(pygame.sprite.Sprite):
    IMAGE = pygame.image.load('bus.png')
    STARTING_POSITION = (400, 250)
    SIZE = (60,30)
    MOVE_DIST = 2

    def __init__(self):
        super().__init__()
        self.image = Bus.IMAGE

        self.rect = pygame.Rect((0,0), Bus.SIZE)
        self.rect.center = Bus.STARTING_POSITION

    def move_left(self):
        self.rect.centerx -= Bus.MOVE_DIST
        if self.rect.centerx <= 0:
            self.rect.centerx = 600

    def move_right(self):
        self.rect.centerx += Bus.MOVE_DIST
        if self.rect.centerx >= 600:
            self.rect.centerx = 0

    

#-----------MAIN-------------#
pygame.init()

# Pygame Variables
SCREEN_DIM = WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode(SCREEN_DIM)
DISPLAY = pygame.display.set_caption('Frogger')
CLOCK = pygame.time.Clock()
FPS = 60


# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)



# Create objects
bus1 = Bus()
log1 = Log()
frog = Frog()



while True:
    CLOCK.tick(FPS)
    SCREEN.fill(BLACK)

    # Draw background (road/water)
    pygame.draw.rect(SCREEN, (200, 206, 207), (0,225,600,100))
    pygame.draw.rect(SCREEN, BLUE, (0,75,600,100))

    # Draw the sprites
    SCREEN.blit(frog.image, frog.rect)
    SCREEN.blit(bus1.image, bus1.rect)
    SCREEN.blit(log1.image, log1.rect)

    # Move the obstacles
    bus1.move_left()
    log1.move_left()

    if frog.rect.colliderect(bus1.rect):
        frog.collision()

    # Update the screen
    pygame.display.flip()

    

    # Continuous game loop
    for event in pygame.event.get():
        # Close the game
        if event.type == pygame.QUIT:
            pygame.quit()
        # Arrow key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:      # Left Key
                frog.move_left()
            if event.key == pygame.K_RIGHT:     # Right Key
                frog.move_right()
            if event.key == pygame.K_UP:        # Up Key
                frog.move_up()
            if event.key == pygame.K_DOWN:      # Down Key
                frog.move_down()

        
        
    
     


        
