# from package.module import create_message as hello
# from package.module1 import create_message as fuck
#
# # используем alias для функции с одинаковым названием - привет
# print(hello('Ivan'))
# # используем alias для функции с одинаковым названием - динах
# print(fuck('Ivan'))

from package.module import toxic_function
# выполняется пока не закончится список
# names = ["Alex", "Ivan", "Artur", "Nikita"]
#
# for name in names:
#     toxic_function(name)

# выполняется пока не выполнится условие
name = None
while name != "Nikita":
    name = input("Enter name: ")
    toxic_function(name)

