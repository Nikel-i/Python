import os
import shutil
mode = input("Если вы хотите скопировать 1 файл, то введите 1. Если всю директорию, то введите 2. Папка для скопированной директории не должна существовать, она создастся автоматически: ")
OriginPath = input("Введите путь к папке из которой копировать файлы: ")
CopyPath = input("Введите путь к папке в которую копировать файлы: ")
if mode == 1:
    try:
        shutil.copy(OriginPath, CopyPath)
    except:
        print("Указан не верный путь")
if mode == 2:
    try:
        shutil.copytree(OriginPath, CopyPath)
    except:
        print("Указан не верный путь")
else:
    print("Что то пошло не так")
