def count_vowels(word):
    # Функция, которая считает количество гласных букв в слове на русском языке
    vowels = "аеёиоуыэюя"
    count = 0
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count

def check_rhythm(poem):
    # Функция, которая проверяет, есть ли ритм в стихотворении
    words = poem.split()
    counts = [count_vowels(word.replace('-', '')) for word in words]
    return len(set(counts)) == 1

# Запрашиваем стихотворение у пользователя
poem = input("Введите стихотворение: ")

# Проверяем, есть ли ритм в стихотворении, и выводим соответствующий ответ
if check_rhythm(poem):
    print("Парам пам-пам")
else:
    print("Пам парам")