def Value (a, b, l, N):

    number = N - 1
    distance = number * b
    row_distance = (N - 1) * a
    cord = distance + row_distance + l

    return cord

a = int(input("Відстань між рядами (a): "))
b = int(input("Відстань між дірочками в ряді (b): "))
l = int(input("Довжину вільного кінця шнурка (l): "))
N = int(input("Кількість дірочок у кожному ряді (N): "))

cord_2 = Value (a, b, l, N)
print("Довжина шнурка: ", cord_2)
