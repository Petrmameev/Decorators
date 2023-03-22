from Exercise2 import logger

documents = [{
    "type": "passport",
    "number": "2207 876234",
    "name": "Василий Гупкин"
}, {
    "type": "invoice",
    "number": "11-2",
    "name": "Геннадий Покемонов"
}, {
    "type": "insurance",
    "number": "10006",
    "name": "Аристарх Павлов"
}]

directories = {'1': ['2207 876234', '11-2'], '2': ['10006'], '3': []}
print("""Введите 'p' - чтобы найти человека по номеру докуммента
Введите 's' - чтобы узнать по номеру документа на какой полке он находится
Введите 'l' - чтобы получить список всех документов
Введите 'a' - чтобы внести новый документ
Введите 'd' - чтобы удалить документ
Введите 'm' - чтобы переместить документ
Введите 'as' - чтобы создать полку

""")

@logger('log_1.log')
def people(documents):
    number_input = input('Введите номер документа')
    for peoples in documents:
        if peoples['number'] == number_input:
            return (peoples.get("name"))
    else:
        return (f'Документа с номером {number_input} нет в базе данных')

@logger('log_2.log')
def shelf(directories):
    number_input = input('Введите номер документа')
    for key in directories:
        if number_input in directories[key]:
            return (f'Документы находятся на полке {key}')
    else:
        return (f'Документа с номером {number_input} нет в базе данных')

@logger('log_3.log')
def add(documents, directories):
    number_directories = input('Введите номер полки для хранения')
    if number_directories not in directories:
        return ('Такой номер полки не существует')
    number = input('Введите номер документа')
    type = input('Введите тип документа')
    name = input('Введите Имя и Фамилию')
    one_document = {'type': type, 'number': number, 'name': name}
    documents.append(one_document)
    directories[number_directories].append(number)
    return ('Данные добавлены')


def list_(documents):
    res = []
    for document in documents:
        res.append(
            f'{document["type"]} "{document["number"]}" "{document["name"]}"')
    return ("\n".join(res))


def delete(documents, directories):
    input_number = input('Введите номер документа который хотите удалить: ')
    for number_shelf, number_documents in directories.items():
        if input_number in number_documents:
            number_documents.remove(input_number)
            break
    else:
        return ('Такого документа нет в базе данных')
    for doc in documents:
        if doc['number'] == input_number:
            documents.remove(doc)
            return ('Документ удален')


def add_shelf(directories):
    new_shelf = input('Введите номер новой полки')
    if new_shelf in directories:
        return ('Такая полка уже существует')
    directories[new_shelf] = []
    return ('Полка создана')


def move(directories):
    input_number_documents = input('Введите номер документа')
    for number_document in directories.values():
        for a in number_document:
            if input_number_documents in number_document:
                input_number_shelf = input(
                    'Введите номер полки на которую хотите переместить документ'
                )
                for number_shelf in directories.keys():
                    if input_number_shelf in number_shelf:
                        number_document.remove(input_number_documents)
                        directories[input_number_shelf].append(
                            input_number_documents)
                        print(directories)
                        return (
                            f'Документ перемещен на {input_number_shelf} полку'
                        )
                else:
                    return ('Такой полки не существует')
    else:
        return ('Документа с таким номером нет в базе данных')


while True:
    command = input('Введите команду: ')
    if command == 'p':
        print(people(documents))
    elif command == 's':
        print(shelf(directories))
    elif command == 'l':
        print(list_(documents), end="\n")
    elif command == 'd':
        print(delete(documents, directories))
    elif command == 'as':
        print(add_shelf(directories))
    elif command == 'm':
        print(move(directories))
    elif command == 'a':
        print(add(documents, directories))
    else:
        print('Такой команды нет')

