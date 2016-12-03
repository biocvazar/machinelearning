from locale import atoi, atof
import random

__author__ = 'Bio'
######################## 1.1
# def herone(triangle_list):
#     a, b, c = triangle_list
#     p = sum(triangle_list)/2
#     return (p * (p - a) * (p - b) * (p - c)) ** 0.5
#
# a = []
# for i in range(3):
#     a.append(atoi(input("Введіть " + str(i+1) +" досжину сторін трикутника: ")))
# print("Площа трикутника: ")
# print(herone(a))


########################## 1.2
# i = 2
# while i <= 14:
#     print(i, "\t", i**4)
#     i += 2

########################## 2.1

# year = atoi(input("Введіть рік\n"))
# print("Високосний" if not year % 4 else "Невисокосний")

########################## 2.2
# flag = True
# while flag:
#     number = atoi(input("Введіть ціле число"))
#     if number < 10:
#         print("Введіть число більше 10")
#     else:
#         print("Ви ввели ", number)
#         flag = False

########################## 3.1
# a = [random.randint(1, 1000) for _ in range(15)]
# print("Елементи: ", a, "\nСума: ", sum(a))

########################## 3.2


def heapsort(array):
    size = len(array)

    for first in range(size//2-1, -1, -1):
        shift(array, first, size)

    for last in range(size-1, 0, -1):
        if array[0] > array[last]:
            array[last], array[0] = array[0], array[last]
            shift(array, 0, last)


def shift(array, first, last):
    parent = array[first]

    while first * 2 + 1 < last:
        child = first * 2 + 1
        if child+1 < last and array[child] < array[child + 1]:
            child += 1
        if parent >= array[child]:
            break
        array[first] = array[child]
        first = child
    array[first] = parent
#
#
#
# a = [random.randint(1, 10) for _ in range(10)]
# print("Масив: ", a)
# heapsort(a)
# print("Відсортований масив", a)

########################## 4.1

# def square(a, b):
#     square =  a*b
#     print("Площа прямокутного стола шириною %.1f та довжиною %.1f дорівнює %.2f"%(a, b, square))
#
# square(2, 5.2)

########################## 4.1
def main():
    array = []
    def bublesort(array:list()):
        for _ in range(len(array)):
            for i in range(len(array)-1):
                if array[i] > array[i+1]:
                    array[i], array[i+1] = array[i+1], array[i]

    def elements():
        n = atoi(input("Введіть кількість елементів масиву: "))
        if n > 0:
            for i in range(n):
                array.append(atof(input("Введіть %i-е значення масиву: "%(i+1))))

    elements()
    print("Початковий масив: ", array)
    bublesort(array)
    print("Відсортований масив: ", array)
main()

