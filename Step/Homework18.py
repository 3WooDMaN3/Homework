from random import randint


def task_1_and_2():
    tuple_ = "banana", "strawberrie, banana", "lemon", "apple", "sada-banana", "watermelon", "blueberry", "lemon"
    name = input("Input fruit: ")
    count = 0
    count2 = 0
    for i in tuple_:
        if i == name:
            count += 1
    for i in tuple_:
        if name in i:
            count2 += 1
    return f'Кол-во "целых" слов: {count} | общее кол-во: {count2}'


# print(task_1_and_2())


def task3():
    names = ('Audi', 'BMW', 'Ford', 'Honda', 'Hyundai', 'Kia', 'Lada', 'Mazda')
    list_of_manufacturers = [names[randint(0, len(names) - 1)] for item in range(10)]
    print(tuple(list_of_manufacturers))
    producer = input("Введите производителя: ")
    new_name = input("Введите слово: ")
    for i in range(len(list_of_manufacturers)):
        if producer == list_of_manufacturers[i]:
            list_of_manufacturers[i] = new_name
    list_of_manufacturers = tuple(list_of_manufacturers)
    return list_of_manufacturers


# print(task3())


def task4():
    countries = set()
    while True:
        print(countries)
        choose = int(input("\nВведите номер пункта(1-4): "))
        if choose == 1:
            countries.add(input("Добавте название страны: "))
        elif choose == 2:
            countries.discard(input("Введите страну, которую хотите удалить: "))
        elif choose == 3:
            count = 0
            symbols = input("Введите символы: ")
            #  Я сделал поиск по символам в любом порядке(пример: names - Никита, Артем, Павел, symbols - аН. Вывод: Никита
            for i in countries:
                for el in symbols:
                    if el in i:
                        count += 1
                        if count == len(symbols):
                            print(f"\nРезультат поиска: {i}\n")
        elif choose == 4:
            name = input("Введите страну: ")
            if name in countries:
                print(True)
        else:
            break


# task4()


def task5():
    set1 = "Kiev", "Odessa", "Moscow", "Moscow", "Novgorod", "Baku", "Seul"
    set2 = "Seul", "Tokio", "Ohio", "Barselona", "Moscow"
    set3 = {''}
    while True:
        choose = int(input("\nВведите номер пункта(1-4): "))
        if choose == 1:
            for i in set1:
                for j in set2:
                    if i == j:
                        set3.add(i)
                        set3.discard('')
        elif choose == 2:
            for i in set1:
                if i not in set2:
                    set3.add(i)
                    set3.discard('')
        elif choose == 3:
            for i in set2:
                if i not in set1:
                    set3.add(i)
                    set3.discard('')
        elif choose == 4:
            set3.update(set2, set1)
            set3.discard('')
        else:
            break
        print(set3)


# task5()


def task6():
    players = {
        "Stephen Curry": "191",
        "Draymond Green": "198",
        "Klay Thompson": "198",
        "Andrew Wiggins": "201",
        "Andre Iguodala": "198"
    }

    def add():
        fullname = input("Input full name: ")
        height = int(input("Input height: "))
        players[fullname] = height
        print(f"{fullname} is added to the list! height = {players[fullname]}")

    def delete():
        fullname = input("Input full name: ")
        if fullname in players.keys():
            del players[fullname]
            print(f"{fullname} has been deleated")
        else:
            print(f"{fullname} hasn't been found")

    def find():
        fullname = input("Input full name: ")
        if fullname in players.keys():
            print(f"{fullname} has been found! His height is {players[fullname]}")
        else:
            print(f"{fullname} hasn't been found")

    def change():
        fullname = input("Input full name: ")
        if fullname in players.keys():
            del players[fullname]
            new_fullname = input("Insert full name of the another player: ")
            new_height = int(input("Insert his height: "))
            players[new_fullname] = new_height
            print(f"{fullname} has been changed!")
        else:
            print(f"{fullname} hasn't been found")

    def main_task_6():
        while True:
            select = int(input("Choose option:"
                               "\n1 - add"
                               "\n2 - delete"
                               "\n3 - find"
                               "\n4 - change"
                               "\n5 - print dict"
                               "\nWrite any number: "))
            if select == 1:
                add()
            elif select == 2:
                delete()
            elif select == 3:
                find()
            elif select == 4:
                change()
            elif select == 5:
                print(players)
            else:
                break

    return main_task_6()


# task6()


def task7():
    print("-" * 30, "Firma Programm", "-" * 30)
    info = {}
    users = {}
    def add_new_user():
        name = input("\nInput the name: ")
        email = input("Input email: ")
        number = input("Input the phone number: ")
        position = input("Input the position: ")
        cabinet = input("Input the number of cabinet: ")
        Skype = input("Input the Skype number: ")
        users[name] = info
        info["email"], info["number"], info["position"], info["cabinet"], info["Skype"] = email, number, position, cabinet, Skype
        print("The information has been saved!")

    def delete_name():
        name = input("\nInput the name: ")
        if name in users:
            del users[name]
            print(f"{name} name has been deleated!")
        else:
            print("\nName hasn't been found!")

    def find_name():
        name = input("\nInput the name: ")
        if name in users:
            print(f"Email: {users[name]['email']}")
            print(f"Number: {users[name]['number']}")
            print(f"Position: {users[name]['position']}")
            print(f"Cabinet: {users[name]['cabinet']}")
            print(f"Skype: {users[name]['Skype']}")
        else:
            print("\nName hasn't been found!")

    def change_name():
        name = input("\nInput the name: ")
        if name in users:
            del users[name]
            add_new_user()
        else:
            print("\nName hasn't been found!")

    def main_task7():
        while True:
            select = int(input("Choose option:"
                               "\n1 - add"
                               "\n2 - delete"
                               "\n3 - find"
                               "\n4 - change"
                               "\n5 - print dict"
                               "\nWrite any number: "))
            if select == 1:
                add_new_user()
            elif select == 2:
                delete_name()
            elif select == 3:
                find_name()
            elif select == 4:
                change_name()
            elif select == 5:
                print(users)
            else:
                break
    return main_task7()


#task7()


def task8():
    print("-" * 30, "Library colletion", "-" * 30)
    # the library consists the dict of names. Names consists the dict of info
    info = {"author": "",
            "genre": "",
            "year": "",
            "pages": "",
            "publishing_office": ""
            }
    library = {}

    def add_new_book():
        name = input("\nInput the name of this book: ")
        author = input("Input fullname of the author: ")
        genre = input("Input genre: ")
        year = input("Input the year: ")
        pages = input("Input the quantity of pages: ")
        publishing_office = input("Input the publishing office: ")
        library[name] = info
        info["author"], info["genre"], info["year"], info["pages"], info["publishing_office"] = author, genre, year, pages, publishing_office
        # output = library[name]
        # return output



    def delete_book():
        name = input("\nInput name of this book: ")
        if name in library:
            del library[name]
            print(f"{name} book has been deleated!")
        else:
            print("\nBook hasn't been found!")

    def find_book():
        name = input("\nInput name of this book: ")
        if name in library:
            print(f"Author: {library[name]['author']}")
            print(f"Genre: {library[name]['genre']}")
            print(f"Year: {library[name]['year']}")
            print(f"Pages: {library[name]['pages']}")
            print(f"Publishing office: {library[name]['publishing_office']}")
        else:
            print("\nBook hasn't been found!")

    def change_book():
        name = input("\nInput name of this book: ")
        if name in library:
            del library[name]
            add_new_book()
        else:
            print("\nBook hasn't been found!")

    def main_task8():
        while True:
            select = int(input("Choose option:"
                               "\n1 - add"
                               "\n2 - delete"
                               "\n3 - find"
                               "\n4 - change"
                               "\n5 - print dict"
                               "\nWrite any number: "))
            if select == 1:
                add_new_book()
            elif select == 2:
                delete_book()
            elif select == 3:
                find_book()
            elif select == 4:
                change_book()
            elif select == 5:
                print(library)
            else:
                break
    return main_task8()

# task8()


def main():
    while True:
        select = int(input("Выберите номер задания (задания 1 и 2 объеденены): "))
        if select == 1 or select == 2:
            print(task_1_and_2())
        elif select == 3:
            print(task3())
        elif select == 4:
            task4()
        elif select == 5:
            task5()
        elif select == 6:
            task6()
        elif select == 7:
            task7()
        elif select == 8:
            task8()
        else:
            break


#main()
