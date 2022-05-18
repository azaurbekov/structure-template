# # input + split -> split - разделителем
# a = input().split()

# # map -> это выполение какой-то ФУНКЦИИ на ОБЪЕКТЫ списка
# a = map(int, a)

# # list -> преобразить тип данных map в список
# a = list(a)

# print(a)
# # print(list(map(int, input().split())))

# 1. Получить эти имена в виде списка
# 2. Используя цикл пробежаться по всем элементам
# 3. Сравнить количество букв в слове
# 4. Вывести на экран это имя, если оно больше 10 букв


# names = input().split()
# for name in names:
#     if len(name) > 10:
#         print(name)

# 1. Надо будет получить список возрастов
# 2. Если этот возраст кратен 2, вывести на экран True
# 3. Если этот возраст НЕ кратен 2, вывести на экран False

# input: 1 2 3 4 5 6
# output: False True False True False True

# a_dict = {
#     "name" : "Almas",
#     "age": 18,
#     "married": False,
#     "children": []
# }

# a_dict["children"].append("New child")
# a_dict["married"] = len(a_dict["children"]) > 0

# a_dict["father"] = {}

# a_dict["father"]["name"] = "Maksat"
# a_dict["father"]["age"] = 42
# a_dict["father"]["married"] = True

# print(a_dict)

# b = [
#     {
#         "name": "Name 1",
#         "age": "Age 1"
#     },
#     {
#         "name": "Name 2",
#         "age": "Age 2"
#     },
#     {
#         "name": "Name 3",
#         "age": "Age 3"
#     }
# ]

# for value in b:
#     value["newKey"] = 99
#     print(value)

# print(b)

# p -> занимает ячейку памяти -> арендует квартиру
# p -> изменить какие-то данные -> изменяете интерфейс квартиры

def create_person(name, age):
    return {
        "name": name,
        "age": age
    }

def update_person(obj, name, age):
    obj["name"] = name
    obj["age"] = age

names = []
n = int(input("Сколько значений вы хотите ввести: "))
for i in range(n):
    person = input("Введите данные человека: ").split()
    p = create_person(person[0], person[1])
    names.append(p)

### ВАШ КОД ###

### ВАШ КОД ###

print(names)