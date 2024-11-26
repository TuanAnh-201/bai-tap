import pygame
import random

# Khởi tạo pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Nhặt Hoa Quả")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Các thuộc tính game
clock = pygame.time.Clock()
FPS = 60

# Tạo các đối tượng Hoa Quả
class Fruit:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 50)  # Vị trí ngẫu nhiên trên màn hình
        self.y = 0  # Quả hoa quả sẽ rơi từ trên cùng
        self.size = random.randint(30, 50)  # Kích thước ngẫu nhiên
        self.speed = random.randint(2, 5)  # Tốc độ rơi ngẫu nhiên
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(RED)  # Tạm thời sử dụng hình vuông
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move(self):
        self.y += self.speed  # Quả hoa quả rơi xuống
        self.rect.y = self.y

    def draw(self):
        window.blit(self.image, self.rect)

# Tạo đối tượng giỏ (hoặc nhân vật nhặt hoa quả)
class Basket:
    def __init__(self):
        self.width = 100
        self.height = 30
        self.speed = 8
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(GREEN)  # Màu giỏ là màu xanh
        self.rect = self.image.get_rect()
        self.rect.y = HEIGHT - 50  # Vị trí giỏ ở dưới cùng

    def move(self, mouse_x):
        """Di chuyển giỏ theo vị trí của chuột (trên trục X)."""
        self.rect.centerx = mouse_x  # Cập nhật vị trí giỏ theo chuột

    def draw(self):
        window.blit(self.image, self.rect)

# Game chính
def game():
    basket = Basket()
    fruits = []
    score = 0
    running = True
    missed_fruits = 0
    game_over = False

    while running:
        window.fill(BLACK)  # Xóa màn hình
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Lấy vị trí chuột
        mouse_x, _ = pygame.mouse.get_pos()

        # Di chuyển giỏ theo chuột
        basket.move(mouse_x)

        # Tạo quả hoa quả mới ngẫu nhiên
        if random.random() < 0.02:  # Tạo quả hoa quả với tỉ lệ thấp
            fruits.append(Fruit())

        # Di chuyển và vẽ các quả hoa quả
        for fruit in fruits[:]:
            fruit.move()
            fruit.draw()

            # Kiểm tra va chạm với giỏ
            if basket.rect.colliderect(fruit.rect):
                score += 1  # Tăng điểm nếu bắt được quả
                fruits.remove(fruit)  # Xóa quả đã nhặt

            # Kiểm tra nếu quả rơi xuống dưới và không được nhặt
            if fruit.y > HEIGHT:
                missed_fruits += 1
                fruits.remove(fruit)

        # Kiểm tra điều kiện kết thúc game
        if missed_fruits >= 3:
            game_over = True
            font = pygame.font.SysFont(None, 50)
            game_over_text = font.render("Game Over!", True, YELLOW)
            window.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2))
            break

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
