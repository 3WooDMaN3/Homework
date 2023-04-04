'''Я взял рандомные предложения из интернета (text)'''


file_name = "Homework_main.txt"
text = "The case came to court, and Ross and Ben were tried. The trial did not last very long. Ross and Ben both pleaded not guilty in court. Their lawyer did her best to defend them, but the prosecuting lawyer produced a very strong case against them. After brief deliberations, the jury passed verdict on them. They decided that Ross was guilty, and he was convicted of robbery, but Ben was innocent. The judge acquitted Ben of any involvement in the robbery, but sentenced Ross to three years in prison/jail. As well as a prison sentence, Ross also had to pay a large fine. Ross served two years in prison, but was released from prison a year early. He got time off for good behaviour"

def main_text():
    write_text = ".\n".join(text.split(". "))
    with open(file_name, "w") as file:
        file.write(write_text)


def Task_1(search, replace):
    main_text()
    data = []
    ''' Читаем файл и выполняем поиск'''
    with open(file_name, "r") as file:
        for item in file.readlines():
            if search in item:
                ''' Изменяем значение(я)'''
                item = item.replace(search, replace)
            data.append(item)
        ''' Перезаписываем файл с изменными данными '''
        with open(file_name, "w") as f:
            f.write("".join(data))


#Task_1("case", "!!!Я гуль!!!")


def Task_2 ():
    main_text()
    count = 0
    ''' Читаем файл'''
    with open(file_name, "r") as file:
        for item in file.readlines():
            for word in item.split():
                try:
                    word = int(word)
                except ValueError:
                    pass
                ''' Считаем кол-во слов'''
                if type(word) == str:
                    count += 1
        print(f"Total number of words is {count}")


def Task_3_reverse():
    main_text()
    ''' Читаем файл'''
    new_data = []
    with open(file_name, "r") as file:
        for item in file.readlines():
            data = item.split()[::-1]
            new_data.append(data)

    """Отчистим файл"""
    with open(file_name, "w") as f:
        f.write("")

    """Запишем по новой"""
    with open(file_name, "a") as file:
        for item in new_data:
            file.write(" ".join(item) + "\n")


def Task_4():
    main_text()
    select = int(input("Input the number of string(from 0): "))
    ''' Мой код '''
    new_writer = []
    new_text = []
    with open(file_name, "r") as f:
        new_writer.extend(f.readlines())
        for i in new_writer:
            if i != new_writer[select]: new_text.append(i)

    """Запишем по новой"""
    with open(file_name, "w") as file:
        file.write("".join(new_text))


    ''' нашел укороченный вариант'''
    # f = open(file_name).readlines()
    # f.pop(select)
    # with open(file_name, 'w') as F:
    #     F.writelines(f)


#Task_4
















