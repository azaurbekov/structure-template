def main():
    # dict - key:value

    order = {
        "food": None,
        "count": 0,
        "price": 0
    }

    menu = [{"food": "pizza", "count": 10, "price": 200 }, { "food":"burger", "count": 8, "price": 400 } ]

    while True:
        command = input("Введите команду: ")

        if command == "exit":
            break
        elif command == "add":
            print(menu)
            command_food = input("Введите еду: ")
            command_count = int(input("Сколько штук вам положить: "))

            item_from_menu = None
            for item in menu:
                if item["food"] == command_food:
                    item_from_menu = item
                    item["count"] -= command_count 

            order["food"] = command_food
            order["count"] = command_count
            order["price"] = item_from_menu["price"] * command_count

        elif command == "remove":
            for item in menu:
                if item["food"] == order["food"]:
                    item["count"] += order["count"]
                    order["food"] = None
                    order["count"] = 0
                    order["price"] = 0
        
        elif command == "show":
            print(menu)
            print(order)

if __name__ == "__main__":
    main()

# 1. Запоминает названия всех перемен и функции
# 2. Синтаксический разбор -> ошибки во время комплияции
# 3. Запуск -> ошибка во время запуска
# debug - отладка кода
# refactoring - переделать логику кода