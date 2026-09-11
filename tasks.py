def show_tasks(tasks):
    print("==СПИСОК ЗАДАЧ==")
    for n, t in enumerate(tasks, start=1):
        print(f"{n}. {t}")

def add_tasks(tasks, name):
    tasks.append(name)
    print(f"Задача успешко добавлена: {name}")
