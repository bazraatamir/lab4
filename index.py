# =========================================
# Snake Game – OOP Загварын Заавар
# =========================================

# --- Snake Класс ---
class Snake:
    def __init__(self):
        # Зорилго: Snake-ийн бүх segment болон хөдөлгөөн хадгалах
        # Алхам:
        # 1. self.body: list, segment бүрийн координат хадгалах
        # 2. self.direction: tuple, хөдөлгөөн (эхлээд баруун тийш)
        pass

    def move(self):
        # Зорилго: Snake-г хөдөлгөх
        # Алхам:
        # 1. Толгойны координатыг авч direction-д үндэслэн шинэ координат тооцох
        # 2. Шинэ толгойг body-ийн эхэнд нэмэх
        # 3. Сүүлийг хасах (snake[:-1])
        pass

    def grow(self):
        # Зорилго: Snake-ийг уртасгах
        # Алхам:
        # 1. Сүүлийн segment-г дахин нэмэх
        pass

    def set_direction(self, new_dir):
        # Зорилго: Шинэ чиглэл тогтоох
        # Алхам:
        # 1. Урвуу чиглэл рүү явахгүй байх шалгах
        # 2. Шинэ direction-г тогтоох
        pass

    def check_collision(self):
        # Зорилго: Өөрийн бие болон дэлгэцийн хилтэй мөргөлдөх эсэх
        # Алхам:
        # 1. Толгой дэлгэцийн хилээс гарсан эсэх
        # 2. Толгой өөрийн бие дээр байгаа эсэх
        # 3. Collision бол True, үгүй бол False
        pass

    def draw(self, screen):
        # Зорилго: Snake-г дэлгэц дээр зурна
        # Алхам:
        # 1. Body-ийн segment бүр дээр loop
        # 2. pygame.draw.rect() ашиглан segment-ийг зурна
        pass


# --- Food Класс ---
class Food:
    def __init__(self):
        # Зорилго: Хоолны координатыг хадгалах
        # Алхам:
        # 1. self.position-д random_position() дуудаж координат хадгалах
        pass

    def random_position(self):
        # Зорилго: Санамсаргүй хоолны байрлал үүсгэх
        # Алхам:
        # 1. WIDTH, HEIGHT-г CELL_SIZE-ээр хувааж random x, y үүсгэх
        # 2. (x, y) tuple буцаах
        pass

    def respawn(self):
        # Зорилго: Хоолыг шинэ байрлалд шилжүүлэх
        # Алхам:
        # 1. random_position() дуудаж шинэ координат хадгалах
        pass

    def draw(self, screen):
        # Зорилго: Хоолыг дэлгэц дээр зурна
        # Алхам:
        # 1. pygame.draw.rect() ашиглах
        pass


# --- Game Класс ---
class Game:
    def __init__(self):
        # Зорилго: Тоглоом эхлүүлэх
        # Алхам:
        # 1. pygame.init() дуудах
        # 2. self.screen, self.clock үүсгэх
        # 3. Snake, Food обьект үүсгэх
        # 4. self.score, self.running-г тохируулах
        pass

    def process_events(self):
        # Зорилго: Хэрэглэгчийн оролт (keyboard, quit)
        # Алхам:
        # 1. pygame.event.get() ашиглан event-үүдийг шалгах
        # 2. QUIT бол running = False
        # 3. KEYDOWN бол snake.set_direction() дуудах
        pass

    def update(self):
        # Зорилго: Snake болон тоглоомын төлөв шинэчлэх
        # Алхам:
        # 1. snake.move() дуудаж хөдөлгөх
        # 2. Snake хоол идсэн эсэхийг шалгах
        #     - Хоол идсэн бол snake.grow(), food.respawn(), score += 1
        # 3. Snake collision шалгах
        #     - collision бол running = False
        pass

    def draw(self):
        # Зорилго: Дэлгэц шинэчлэх, snake, food, score зурах
        # Алхам:
        # 1. screen.fill() ашиглаж дэлгэцийг цэвэрлэх
        # 2. snake.draw(screen)
        # 3. food.draw(screen)
        # 4. Оноог font ашиглан зурна
        # 5. pygame.display.flip() дуудна
        pass

    def run(self):
        # Зорилго: Game loop ажиллуулах
        # Алхам:
        # 1. while self.running:
        #     - self.clock.tick(FPS)
        #     - self.process_events()
        #     - self.update()
        #     - self.draw()
        # 2. pygame.quit() дуудна
        pass


# --- Main ---
if __name__ == "__main__":
    # Алхам:
    # 1. Game обьект үүсгэх
    # 2. game.run() дуудаж тоглоом эхлүүлэх
    pass
