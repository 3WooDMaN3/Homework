''' Система "Сотрудники" '''
import json
import csv
info_system = {

}
info_of_users = {

}
count = 0
file_name = r"C:\Users\Professional\PycharmProjects\Step\Sotrudniki_system"
extension_csv = ".csv"
extension_json = ".json"
def add_user():
    global count
    full_name = input("Input user's fullname: ")
    age = input("Input the age: ")
    email = input("Input email: ")
    number = input("Input the phone number: ")
    position = input("Input the position: ")
    Skype = input("Input the Skype number: ")
    hobby = input("Input the hobby: ")
    info_of_users["age"], info_of_users["email"], info_of_users["number"], info_of_users["position"], info_of_users["Skype"], info_of_users["hobby"] = age, email, number, position, Skype, hobby
    print("The information has been saved!")
    info_system[full_name] = info_of_users.copy()
    def csv_record():
        with open(file_name + extension_csv, "a", newline="", encoding="cp1251") as file:
            '''В excel иногда все пишет в одном столбике, используя delimiter=';', я это исправил'''
            writer = csv.writer(file, delimiter=";")
            writer.writerow((full_name,
                             age,
                             email,
                             number,
                             position,
                             Skype,
                             hobby))
        csv_record()

def delete_name():
    print("!!If you delete fullname, the information also will be deleated!!")
    name = input("Input the name: ")
    if name in info_system:
        del info_system[name]
        print(f"{name} name has been deleated!")
    else:
        print("\nName hasn't been found!")


def find_full_info():
    name = input("\nInput the name: ")
    if name in info_system:
        print(f"Age: {info_system[name]['age']}")
        print(f"Email: {info_system[name]['email']}")
        print(f"Number: {info_system[name]['number']}")
        print(f"Position: {info_system[name]['position']}")
        print(f"Skype: {info_system[name]['Skype']}")
        print(f"Hobby: {info_system[name]['hobby']}")
    else:
        print("\nName hasn't been found!")


def change_name():
    name = input("\nInput the name: ")
    if name in info_system:
        del info_system[name]
        add_user()
    else:
        print("\nName hasn't been found!")


def print_all_users_info():
    for i in info_system.items():
        print(i)


def search_first_letter():
    letter = input("Input the first letter of name: ")
    count = 0
    for i in info_system.keys():
        print(i[0])
        if letter == i[0]:
            count += 1
            print(i, end=": ")
            print(info_system[i])
    if count == 0:
        print("Nothing found")


def search_age():
    name = input("Input the name: ")
    if name in info_system.keys():
        print(f"Age: {info_system[name]['age']}")
    else:
        print("\nName hasn't been found!")


def change_data():
    name = input("Input the name: ")
    if name in info_system:
        select = input("Input the option, which you want to change"
                       "(age, email, number, position, Skype, hobby):  ")
        if select == "age":
            new_age = input("Input the age: ")
            info_system[name]["age"] = new_age
            print("The information has been saved!")
        elif select == "email":
            new_email = input("Input the email: ")
            info_system[name]["email"] = new_email
            print("The information has been saved!")
        elif select == "number":
            new_number = input("Input the phone number: ")
            info_system[name]["number"] = new_number
            print("The information has been saved!")
        elif select == "Skype":
            new_Skype = input("Input the Skype number: ")
            info_system[name]["Skype"] = new_Skype
            print("The information has been saved!")
        elif select == "hobby":
            new_hobby = input("Input the hobby: ")
            info_system[name]["hobby"] = new_hobby
            print("The information has been saved!")
        else:
            print("You have written the wrong option!")
    else:
        print("\nName hasn't been found!")


def record():
    with open(file_name + extension_json, "w") as file:
        json.dump(info_system, file, indent=4, ensure_ascii=False)

def main():
    with open(file_name + extension_csv, "w", newline='', encoding="cp1251") as file:
        '''В excel иногда все пишет в одном столбике, используя delimiter=';', я это исправил'''
        writer = csv.writer(file, delimiter=";")
        writer.writerow(("fullname",
                         "age",
                         "email",
                         "number",
                         "position",
                         "Skype",
                         "hobby"))
    while True:
        select = int(input("Choose option:"
                           "\n1 - add"
                           "\n2 - delete"
                           "\n3 - find"
                           "\n4 - change"
                           "\n5 - print dict"
                           "\n6 - search first letter"
                           "\n7 - search age"
                           "\n8 - change data"
                           "\n9 - record to json format"
                           "\nWrite any number: "))
        if select == 1:
            add_user()
        elif select == 2:
            delete_name()
        elif select == 3:
            find_full_info()
        elif select == 4:
            change_name()
        elif select == 5:
            print_all_users_info()
        elif select == 6:
            search_first_letter()
        elif select == 7:
            search_age()
        elif select == 8:
            change_data()
        elif select == 9:
            record()
        else:
            break




if __name__ == '__main__':
    main()