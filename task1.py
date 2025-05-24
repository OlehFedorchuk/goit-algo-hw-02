import queue
import time
import random

# Створення черги заявок
request_queue = queue.Queue()
request_id = 1  # Ідентифікатор для заявок

def generate_request():
    global request_id
    # Створення нової заявки
    request = f"Заявка #{request_id}"
    request_id += 1
    # Додавання заявки до черги
    request_queue.put(request)
    print(f"[Генерація] Додано {request}")

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"[Обробка] Обробляється {request}")
        time.sleep(random.uniform(0.5, 2))  # Імітація часу обробки
        print(f"[Обробка] Завершено {request}")
    else:
        print("[Обробка] Черга пуста. Немає заявок для обробки.")

def main_loop():
    try:
        while True:
            generate_request()
            time.sleep(random.uniform(0.5, 1.5))  # Імітація часу між надходженням заявок
            process_request()
    except KeyboardInterrupt:
        print("\n[Завершення] Програма зупинена користувачем.")

if __name__ == "__main__":
    main_loop()