def print_operation_table(operation, num_rows=6, num_columns=6):
    # Печатаем заголовок таблицы
    print("  ", end="")
    for j in range(1, num_columns+1):
        print(j, end=" ")
    print()

    # Печатаем строки таблицы
    for i in range(1, num_rows+1):
        print(i, end=" ")
        for j in range(1, num_columns+1):
            result = operation(i, j)
            print(result, end=" ")
        print()

# Запрашиваем у пользователя значения num_rows и num_columns
num_rows = int(input("Введите число строк: "))
num_columns = int(input("Введите число столбцов: "))

# Вызываем функцию print_operation_table с заданными аргументами
print_operation_table(lambda x, y: x * y, num_rows, num_columns)