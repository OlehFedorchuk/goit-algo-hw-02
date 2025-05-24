from collections import deque

def is_palindrome(input_string):
    # Попередня обробка: видалення пробілів і переведення в нижній регістр
    cleaned = ''.join(char.lower() for char in input_string if char.isalnum())
    
    # Додаємо символи до двосторонньої черги
    char_deque = deque(cleaned)
    
    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("racecar"))                      # True
print(is_palindrome("Hello"))                        # False
print(is_palindrome("ollo"))                         # True