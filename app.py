import streamlit as st
import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Thiết lập các thông số trò chơi
WIDTH, HEIGHT = 400, 600
BIRD_WIDTH, BIRD_HEIGHT = 40, 40
PIPE_WIDTH, PIPE_HEIGHT = 70, 400
GAP = 150

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Thiết lập cửa sổ trò chơi
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Tạo lớp Bird
class Bird:
    def __init__(self):
        self.x = WIDTH // 4
        self.y = HEIGHT // 2
        self.gravity = 0.6
        self.lift = -15
        self.velocity = 0

    def show(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT))

    def update(self):
        self.velocity += self.gravity
        self.velocity *= 0.9
        self.y += self.velocity

        if self.y > HEIGHT:
            self.y = HEIGHT
            self.velocity = 0

        if self.y < 0:
            self.y = 0
            self.velocity = 0

    def up(self):
        self.velocity += self.lift

# Tạo lớp Pipe
class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.top = random.randint(50, HEIGHT // 2)
        self.bottom = HEIGHT - self.top - GAP
        self.w = PIPE_WIDTH
        self.speed = 5

    def show(self):
        pygame.draw.rect(screen, GREEN, (self.x, 0, self.w, self.top))
        pygame.draw.rect(screen, GREEN, (self.x, HEIGHT - self.bottom, self.w, self.bottom))

    def update(self):
        self.x -= self.speed

    def offscreen(self):
        return self.x < -self.w

    def hits(self, bird):
        if bird.y < self.top or bird.y > HEIGHT - self.bottom:
            if bird.x > self.x and bird.x < self.x + self.w:
                return True
        return False

# Hàm để chạy trò chơi Pygame
def run_game():
    bird = Bird()
    pipes = []
    pipes.append(Pipe())

    running = True
    score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.up()

        bird.update()

        if pipes[0].offscreen():
            pipes.pop(0)

        if len(pipes) < 1 or pipes[-1].x < WIDTH // 2:
            pipes.append(Pipe())

        for pipe in pipes:
            pipe.update()
            if pipe.hits(bird):
                running = False

        screen.fill(WHITE)
        bird.show()
        for pipe in pipes:
            pipe.show()

        pygame.display.update()

    pygame.quit()

# Tạo một nút bấm trong Streamlit để khởi động trò chơi
if st.button("Chơi Flappy Bird"):
    run_game()
