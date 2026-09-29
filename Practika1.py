import random

#task1
degrees_celsius = float(input())
print(f'{degrees_celsius}°C = {(degrees_celsius * 9 / 5) + 32:.2f}°F')
print(f'{degrees_celsius}°C = {degrees_celsius + 273.15:.2f}K')

#task2
number = int(input())
if number % 2 == 0:
    print('чётное', end=', ')
else:
    print('нечётное', end=', ')
if number > 0:
    print('положительное', end=', ')
else:
    print('отрицательное', end=', ')
if 10 <= number <= 50:
    print('принадлет промежутку', end='.\n')
else:
    print('непринадлет промежутку', end='.\n')

#task3
print("Сгенерированный пароль:", end=' ')
def generate_password():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    specials = "!@#$%^&*"

    p1 = random.choice(letters) + random.choice(letters) + random.choice(letters)
    p2 = random.choice(digits) + random.choice(digits) + random.choice(digits)
    p3 = random.choice(specials) + random.choice(specials)

    all_chars = list(p1 + p2 + p3)
    random.shuffle(all_chars)

    return "".join(all_chars)


password = generate_password()
print("Ваш пароль:", password)

#task4
def analyze_text():
    text = input().lower()

    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    print("3 самых частых символа:")
    for _ in range(3):
        if not counts:
            break
        max_char = max(counts, key=counts.get)
        print(f"{max_char}: {counts[max_char]}",)
        del counts[max_char]


analyze_text()

#task5
N = int(input())
primes = list(range(2, N + 1))

i = 0
while i < len(primes):
    p = primes[i]
    if p != 0:  
        j = i + p
        while j < len(primes):
            primes[j] = 0
            j += p
    i += 1

primes = [x for x in primes if x != 0]
print(*primes)

#task6
def find_digit():
    n = int(input())

    length = 1
    count = 9
    start = 1

    while n > length * count:
        n -= length * count
        length += 1
        count *= 10
        start *= 10

    num = start + (n - 1) // length
    digit_index = (n - 1) % length

    print(str(num)[digit_index])


find_digit()

