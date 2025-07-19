# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 14:24:42 2025

@author: cvsen
"""

import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker - Green Background")

# Colors
WHITE = (255, 255, 255)
PADDLE_COLOR = (255, 255, 0)
BRICK_COLOR = (200, 0, 0)
BG_COLOR = (0, 128, 0)  # Green

# Clock
clock = pygame.time.Clock()

# Ball settings
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 4
ball_dy = -4

# Paddle settings
paddle_width = 100
paddle_height = 10
paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - 40
paddle_speed = 7

# Brick settings
brick_rows = 5
brick_cols = 10
brick_width = WIDTH // brick_cols
brick_height = 30
bricks = []

for row in range(brick_rows):
    for col in range(brick_cols):
        brick_rect = pygame.Rect(col * brick_width, row * brick_height + 50, brick_width - 5, brick_height - 5)
        bricks.append(brick_rect)

# Game loop
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    # Move ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Wall collision
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_dx *= -1
    if ball_y - ball_radius < 0:
        ball_dy *= -1

    # Paddle collision
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    if paddle_rect.collidepoint(ball_x, ball_y + ball_radius):
        ball_dy *= -1

    # Brick collision
    hit_index = -1
    for i, brick in enumerate(bricks):
        if brick.collidepoint(ball_x, ball_y - ball_radius):
            hit_index = i
            ball_dy *= -1
            break
    if hit_index >= 0:
        del bricks[hit_index]

    # Game over
    if ball_y > HEIGHT:
        print("Game Over!")
        running = False

    # Win condition
    if not bricks:
        print("You Win!")
        running = False

    # Draw everything
    screen.fill(BG_COLOR)  # Fill background with green
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(screen, PADDLE_COLOR, paddle_rect)
    for brick in bricks:
        pygame.draw.rect(screen, BRICK_COLOR, brick)

    pygame.display.flip()

# Exit
pygame.quit()
sys.exit()

