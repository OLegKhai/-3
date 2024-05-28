from cat import Cat, CatArray

# Створення об'єктів кішок
cat1 = Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий")
cat2 = Cat("Мурзик", "Сіамська", "сірий", 2.5, 4.2, "короткошерстий")
cat3 = Cat("Вася", "Мейн-кун", "чорний", 1.8, 3.7, "довгошерстий")
cat4 = Cat("Леся", "Шотландська", "сірий", 3.2, 2.1, "короткошерстий")
cat5 = Cat("Том", "Рагдолл", "білий", 4.5, 5.8, "довгошерстий")

# Створення масиву кішок
cat_array = CatArray([cat1, cat2, cat3, cat4, cat5])

# Демонстрація роботи різних функцій класу CatArray

# Вивід усіх кішок у масиві
print("All cats in the array:")
for cat in cat_array:
    print(cat)

# Додавання нової кішки до масиву
new_cat = Cat("Пушок", "Британська", "сірий", 2.0, 3.5, "короткошерстий")
cat_array.append(new_cat)
print("\nAdded a new cat:", new_cat)

# Вставка нової кішки на позицію з індексом 2
new_cat = Cat("Борис", "Персидська", "сірий", 3.5, 4.1, "довгошерстий")
cat_array.insert(2, new_cat)
print("\nInserted a new cat at index 2:", new_cat)

# Знаходження кішки з ім'ям "Мурзик" у масиві
target_cat = Cat("Мурзик", "Сіамська", "сірий", 2.5, 4.2, "короткошерстий")
index = cat_array.index(target_cat)
print("\nFound cat:", cat_array[index])

# Видалення кішки з ім'ям "Леся" з масиву
target_cat = Cat("Леся", "Шотландська", "сірий", 3.2, 2.1, "короткошерстий")
cat_array.remove(target_cat)
print("\nRemoved cat:", target_cat)
