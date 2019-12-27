import os

print("Имя пользователя:", os.getlogin())
for i in os.listdir('/Users/' + os.getlogin()):
    print(i)
print("Скрипт запущен из:", os.path.abspath(os.curdir))
