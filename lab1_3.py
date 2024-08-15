N = int(input("Введіть ціле число N (1 < N < 9): "))

# Перевірка, що N у правильному діапазоні
if N <= 1 or N >= 9:
    print("N має бути в межах від 2 до 8!")
else:
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            print(j, end=" ")
        print()
