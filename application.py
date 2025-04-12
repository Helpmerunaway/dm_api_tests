from package.module import create_message as hello
from package.module1 import create_message as fuck

# используем alias для функции с одинаковым названием - привет
print(hello('Ivan'))
# используем alias для функции с одинаковым названием - динах
print(fuck('Ivan'))
