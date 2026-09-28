text = input("Введіть текст латинськими літерами: ")

# Формуємо множину з усіх унікальних символів, що є в тексті
unique_chars = set(text)

# Створюємо порожню множину для результату
repeated_letters = set()

for char in unique_chars:
    # Перевіряємо, чи це літера (щоб не враховувати пробіли чи цифри)
    if char.isalpha():
        # Якщо кількість входжень літери 2 і більше
        if text.count(char) >= 2:
            repeated_letters.add(char)

print("Літери, що трапляються не менше двох разів:", repeated_letters)