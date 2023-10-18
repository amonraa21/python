import os

print(f'Папка: {os.getcwd()}')

if not os.path.isdir('Folder'):
    os.mkdir('Folder')

os.chdir()