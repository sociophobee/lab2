# Введення речення
sentence = input("Введіть речення (мінімум 7 слів): ")

# Переводимо все в нижній регістр і прибираємо зайві розділові знаки
clean_text = sentence.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '')
words = clean_text.split()

if len(words) < 7:
    print("Помилка: ви ввели менше 7 слів.")
else:
    print("Слова, які зустрічаються лише один раз:")
    for word in words:
        # count рахує скільки разів слово є у списку
        if words.count(word) == 1:
            print("-", word)