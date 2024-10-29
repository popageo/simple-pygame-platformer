import pygame
from settings import WIDTH, HEIGHT, FPS
from player import Player
from objects import Fire, Block, StartCP
from helpers import get_block, get_background, draw
from collision import handle_move


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Pink.png")

    block_size = 96
    player = Player(155, 100, 50, 50)
    fire = Fire(300, HEIGHT - block_size - 64, 16, 32)
    fire1 = Fire(500, HEIGHT - block_size - 64, 16, 32)
    fire.off()
    fire1.on()
    checkpoint = StartCP(100, HEIGHT - block_size - 128, 64, 64)

    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
    objects = [*floor, Block(0, HEIGHT - block_size * 2, block_size),
               Block(block_size * 3, HEIGHT - block_size * 4, block_size),
               Block(block_size * 4, HEIGHT - block_size * 4, block_size),
               Block(block_size * 5, HEIGHT - block_size * 4, block_size),
               Block(block_size * 6, HEIGHT - block_size * 4, block_size),
               Block(block_size * 6, HEIGHT - block_size * 5, block_size),
               checkpoint, fire, fire1]
    
    offset_x = 0
    scroll_area_width = 200

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP and player.jump_count < 2:
                    player.jump()

        player.loop(FPS)
        fire.loop()
        fire1.loop()
        checkpoint.loop()
        handle_move(player, objects)
        draw(window, background, bg_image, player, objects, offset_x)

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel

    pygame.quit()

if __name__ == "__main__":
    main(window)
