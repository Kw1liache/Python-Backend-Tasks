import random
import string


#task 1
def detect_language(text: str) -> str:
    #Определяет язык текста по первой найденной букве.
    for char in text:
        if 'a' <= char.lower() <= 'z':
            return 'en'
        if 'а' <= char.lower() <= 'я' or char.lower() == 'ё':
            return 'ru'
    return 'en'


def caesar_cipher(text: str, shift: int, decrypt: bool = False) -> str:
    #Шифрует или дешифрует текст шифром Цезаря.
    if decrypt:
        shift = -shift

    result = ''
    for char in text:
        if 'a' <= char.lower() <= 'z':
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            idx = alphabet.index(char.lower())
            new_char = alphabet[(idx + shift) % 26]
            result += new_char.upper() if char.isupper() else new_char
        elif 'а' <= char.lower() <= 'я' or char.lower() == 'ё':
            alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            idx = alphabet.index(char.lower())
            new_char = alphabet[(idx + shift) % 33]
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

text = 'Привет мир'
encrypted = caesar_cipher(text, 3)
decrypted = caesar_cipher(encrypted, 3, decrypt=True)
print(f'Оригинал:    {text}')
print(f'Шифр:        {encrypted}')
print(f'Дешифр:      {decrypted}')

text_en = "Hello World"
encrypted_en = caesar_cipher(text_en, 5)
decrypted_en = caesar_cipher(encrypted_en, 5, decrypt=True)
print(f"Original:    {text_en}")
print(f"Encrypted:   {encrypted_en}")
print(f"Decrypted:   {decrypted_en}")
print(f"Язык '{text}': {detect_language(text)}")
print(f"Язык '{text_en}': {detect_language(text_en)}")

#task 2
def check_winners(scores, student_score):
    set_scores = sorted(scores, reverse=True)
    k = 0
    for i in set_scores[0:3]:
        if i == student_score:
            k += 1
    if k == 0:
        print('Вы не попали в тройку победителей.')
    else:
        print('Вы в тройке победителей!')
# Вызовы для проверки работы функции check_winners().
# Три набора данных - для проверки разных ситуаций.
first_olympiad_scores = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28, 42, 40, 39, 1, 45, 37, 10, 31, 27, 17, 46, 2, 22, 35, 55]
check_winners(first_olympiad_scores, 52)

#task 3
def print_pack_report(starting_value):
    # Объявите диапазон от starting_value до 1 включительно
    # и переберите его в цикле:
    for number in range(starting_value, 0, -1):
        # Проверьте, делится ли текущий элемент
        # на 3, на 5 и на 3 и 5 одновременно.
        # В зависимости от результата проверки
        # напечатайте нужную фразу
        if number % 3 == 0 and number % 5 == 0:
            print(f'{number} - расфасуем по 3 или по 5')
        elif number % 3 == 0 and number % 5 != 0:  
            print(f'{number} - расфасуем по 3')
        elif number % 3 != 0 and number % 5 == 0:  
            print(f'{number} - расфасуем по 5')
        else:
            print(f'{number} - не заказываем!')

# Тесты
print_pack_report(31)
print_pack_report(1)
print_pack_report(0)

#task 4
def generate_password(
    length: int = 12,
    use_lower: bool = True,
    use_upper: bool = True,
    use_digits: bool = True,
    use_special: bool = True,
) -> str:
    #Генерирует пароль с заданными параметрами.
    pool = ''
    required = []

    if use_lower:
        pool += string.ascii_lowercase
        required.append(random.choice(string.ascii_lowercase))
    if use_upper:
        pool += string.ascii_uppercase
        required.append(random.choice(string.ascii_uppercase))
    if use_digits:
        pool += string.digits
        required.append(random.choice(string.digits))
    if use_special:
        pool += string.punctuation
        required.append(random.choice(string.punctuation))

    if not pool:
        return ''  # Возвращаем пустую строку, если нет выбранных категорий

    remaining = length - len(required)
    remaining = max(remaining, 0)

    password = required + [random.choice(pool) for _ in range(remaining)]
    random.shuffle(password)
    return "".join(password)


def main() -> None:
    """Интерфейс генератора паролей."""
    print("=" * 40)
    print("   🔐 ГЕНЕРАТОР ПАРОЛЕЙ")
    print("=" * 40)

    length = int(input("\n📏 Длина пароля: "))
    use_lower = input("🔡 Нижний регистр (да/нет): ").strip().lower() == "да"
    use_upper = input("🔠 Верхний регистр (да/нет): ").strip().lower() == "да"
    use_digits = input("🔢 Цифры (да/нет): ").strip().lower() == "да"
    use_special = input("✨ Спецсимволы (да/нет): ").strip().lower() == "да"

    password = generate_password(length, use_lower, use_upper, use_digits, use_special)

    print("\n" + "=" * 40)
    print(f"   Ваш пароль: {password}")
    print("=" * 40)


if __name__ == "__main__":
    main()

#task 5
def int_to_roman(num: int) -> str:
    #Конвертирует арабское число в римское.
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    result = ''
    for val, sym in zip(values, symbols):
        while num >= val:
            result += sym
            num -= val
    return result


def roman_to_int(s: str) -> int:
    #Конвертирует римское число в арабское.
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
            result -= roman_map[s[i]]
        else:
            result += roman_map[s[i]]
    return result


# Тесты
roman_tests = ['IV', 'IX', 'XLII', 'XCIX', 'MMXXIII']
for r in roman_tests:
    num = roman_to_int(r)
    back = int_to_roman(num)
    print(f'{r} -> {num} -> {back}')

#task 6
HANGMAN_STAGES = [
    """
     ------
     |    |
     |
     |
     |
     |
    ========""",
    """
     ------
     |    |
     |    O
     |
     |
     |
    ========""",
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ========""",
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ========""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ========""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ========""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ========""",
]


def get_random_word() -> str:
    #Возвращает случайное слово.
    words = ["питон", "функция", "переменная", "алгоритм", "массив",
             "словарь", "условие", "цикл", "модуль", "класс"]
    return random.choice(words)


def display_word(word: str, guessed: set[str]) -> str:
    #Показывает слово с угаданными буквами.
    return " ".join(ch if ch in guessed else "_" for ch in word)


def play_hangman() -> None:
    #Основной цикл игры Виселица.
    word = get_random_word()
    guessed: set[str] = set()
    wrong: set[str] = set()
    max_errors = len(HANGMAN_STAGES) - 1

    print("\nВИСЕЛИЦА\n")

    while len(wrong) < max_errors:
        print(HANGMAN_STAGES[len(wrong)])
        print(f"\nСлово: {display_word(word, guessed)}")
        print(f"Ошибки ({len(wrong)}/{max_errors}): {' '.join(sorted(wrong))}")

        if all(ch in guessed for ch in word):
            print(f"\nПобеда! Слово: {word}")
            return

        letter = input("Введите букву: ").strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Введите одну букву!")
            continue
        if letter in guessed or letter in wrong:
            print("Уже было!")
            continue

        if letter in word:
            guessed.add(letter)
        else:
            wrong.add(letter)

    print(HANGMAN_STAGES[-1])
    print(f"\nПроигрыш! Слово было: {word}")


if __name__ == "__main__":
    play_hangman()
