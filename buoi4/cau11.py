import pygame
import random

# Khởi tạo pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Bắn Chim")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Các thuộc tính game
clock = pygame.time.Clock()
FPS = 60

# Tạo các đối tượng
class Bird:
    def __init__(self):
        self.x = random.randint(600, 800)
        self.y = random.randint(50, 500)
        self.speed = random.randint(2, 5)
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = random.randint(600, 800)
            self.y = random.randint(50, 500)
        self.rect.topleft = (self.x, self.y)

    def draw(self):
        window.blit(self.image, self.rect)

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 5
        self.speed = 7
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        self.x += self.speed
        self.rect.x = self.x

    def draw(self):
        pygame.draw.rect(window, WHITE, self.rect)

# Chức năng kiểm tra va chạm
def check_collision(bird, bullet):
    return bird.rect.colliderect(bullet.rect)

# Chức năng game chính
def game():
    bird = Bird()
    bullets = []
    score = 0
    running = True

    while running:
        window.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Lấy vị trí chuột
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Bắn đạn khi nhấn chuột trái
        if pygame.mouse.get_pressed()[0]:  # Nếu nhấn chuột trái
            bullets.append(Bullet(mouse_x, mouse_y))  # Tạo đạn tại vị trí chuột

        # Di chuyển và vẽ chim
        bird.move()
        bird.draw()

        # Di chuyển và vẽ đạn
        for bullet in bullets:
            bullet.move()
            bullet.draw()

        # Kiểm tra va chạm
        for bullet in bullets:
            if check_collision(bird, bullet):
                score += 1
                bird = Bird()  # Tạo một con chim mới
                bullets.remove(bullet)  # Xóa đạn đã bắn trúng

        # Hiển thị điểm số
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {score}", True, WHITE)
        window.blit(score_text, (10, 10))

        # Cập nhật màn hình
        pygame.display.update()

        # Điều chỉnh tốc độ khung hình
        clock.tick(FPS)

# Chạy game
game()

# Thoát khỏi pygame
pygame.quit()
