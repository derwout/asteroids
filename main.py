import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    asteroid_field = AsteroidField()

    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (shots, updatables, drawables)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player) == True:
                print("Game over!")
                exit()
            for shot in shots:
                if shot.collision_check(asteroid) == True:
                    asteroid.kill()
                    shot.kill()

        screen.fill("black")

        for drawable in drawables:
            drawable.draw(screen)
            
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()