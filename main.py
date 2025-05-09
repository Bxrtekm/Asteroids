import sys
import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
            
        for asteroid in asteroids:
            if player.collision(asteroid):
                sys.exit("Game Over!")

            for bullet in shots:
                if bullet.collision(asteroid):
                    asteroid.split()
                    bullet.kill()

        pygame.display.flip()
        
        #Limiting to 60 FPS
        dt = clock.tick(60) / 1000

    
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()