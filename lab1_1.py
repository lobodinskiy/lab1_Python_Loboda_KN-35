# Введення значень a та b з перевіркою
def input_value(name):
    while True:
        try:
            value = int(input(f"Введіть значення {name} (від 1 до 100): "))
            if 1 <= value <= 100:
                return value
            else:
                print("Значення має бути від 1 до 100.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

a = input_value("a")
b = input_value("b")

# Обчислення X на основі умов
if a > b:
    x = 2 * a + b
elif a == b:
    x = -2
else:
    x = (a - 5) / b

# Виведення результату
print(f"Результат: X = {x}")
