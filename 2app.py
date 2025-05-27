import pygame
import random

# 초기 설정
pygame.init()

# 화면 설정
WIDTH = 800
HEIGHT = 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("공룡 점프 게임")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 시계
clock = pygame.time.Clock()
FPS = 60

# 공룡 설정
dino_width = 50
dino_height = 50
dino_x = 50
dino_y = HEIGHT - dino_height - 30
dino_vel_y = 0
gravity = 0.8
is_jumping = False

# 장애물 설정
obstacle_width = 20
obstacle_height = 40
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height - 30
obstacle_speed = 7

# 점수
score = 0
font = pygame.font.SysFont(None, 36)

def draw_window():
    win.fill(WHITE)

    # 공룡 그리기
    pygame.draw.rect(win, BLACK, (dino_x, dino_y, dino_width, dino_height))

    # 장애물 그리기
    pygame.draw.rect(win, BLACK, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # 점수 표시
    score_text = font.render(f"Score: {score}", True, BLACK)
    win.blit(score_text, (10, 10))

    pygame.display.update()

def main():
    global dino_y, dino_vel_y, is_jumping, obstacle_x, score

    run = True
    while run:
        clock.tick(FPS)

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # 키 입력 처리
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not is_jumping:
            is_jumping = True
            dino_vel_y = -15

        # 중력 및 점프
        if is_jumping:
            dino_y += dino_vel_y
            dino_vel_y += gravity

            if dino_y >= HEIGHT - dino_height - 30:
                dino_y = HEIGHT - dino_height - 30
                is_jumping = False

        # 장애물 이동
        obstacle_x -= obstacle_speed
        if obstacle_x < -obstacle_width:
            obstacle_x = WIDTH + random.randint(300, 600)
            score += 1

        # 충돌 판정
        if (
            dino_x < obstacle_x + obstacle_width and
            dino_x + dino_width > obstacle_x and
            dino_y + dino_height > obstacle_y
        ):
            print("게임 오버!")
            run = False

        draw_window()

    pygame.quit()

if __nam
