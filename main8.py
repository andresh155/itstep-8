import random
def select_task():
    task = input("виберіть задавдання: 1-5 ")
    match task:
        case "1":
            task1()
        case "2":
            task2()
        case "3":
            task3()
        case "4":
            task4()
        case "5":
            task5()
        case "exit":
            exit()
        case _:
            print("невірний вибір, спробуйте ще раз")
            select_task()
def task1():
    n1 = int(input("введіть число: "))
    for i in range(1, 11):
        print(n1, "*", i, "=", n1 * i)

def task2():
    for i in range(1, 11):
        for j in range(1, 10):
            print(i, "*", j, "=", i * j)
        print("------------------")
def task3():
    n1 = int(input("введіть кількість чисел: "))
    the_biggest = 0
    for i in range(n1):
        n2 = int(input("введіть число: "))
        if n2 > the_biggest:
            the_biggest = n2
    print("найбільше число:", the_biggest)
def task4():
    n1 = random.randint(1, 500)
    print("напишіть число від 1 до 500")
    attempts = 0
    while True:
        n2 = int(input("введіть число: "))
        attempts += 1
        if n2 == n1:
            print("вітаю, ви вгадали число!")
            print("кількість спроб:", attempts)
            break
        elif n2 > n1:
            print("загадане число менше")
        else:
            print("загадане число більше")
def task5():
    match int(input("1.квадрат 2. прямокутник ")):
        case 1:
            n1 = int(input("введіть довжинусторону квадрата: "))
            h1 = input("введіть символ: ")
            for i in range(n1):
                print(h1 * n1)
        case 2:
            n1 = int(input("введіть довжину прямокутника: "))
            n2 = int(input("введіть ширину прямокутника: "))
            h1 = input("введіть символ: ")
            for i in range(n2):
                print(h1 * n1)
        case _:
            print("невірний вибір")
while True:
    select_task()