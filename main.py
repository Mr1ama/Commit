from tasks import *

projects = [
    "Создать проект",
    "Сделать коммит",
    "Написать функцию"
]

new_task = input("Введите новую задачу: ")
add_tasks(projects, new_task)

show_tasks(projects)