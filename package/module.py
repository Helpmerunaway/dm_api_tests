name = 'Artur'

def create_message(name):
    """
    This func printing Hello message
    :param name:
    :return:
    """
    message = "Hello, " + name
    return message

def printing_message(name):
    message = create_message(name)
    print(message)

# запуск исполяемого кода в текущем модуле
if __name__ == '__main__':
    match name:
        case 'Ivan':
            printing_message(name)
        case 'Artur':
            printing_message(name)
        case 'Nikita':
            printing_message(name)
        case _:
            print('Fuck you')

