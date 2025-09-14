import json


class Task:

    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }


class TaskManager:

    def __init__(self, storage=None):
        self.tasks = []
        self.storage = storage
        if self.storage:
            self.tasks = self.storage.load()

    def add_task(self, task):
        self.tasks.append(task)
        if self.storage:
            self.storage.save(self.tasks)

    def remove_task(self, title):
        for t in self.tasks:
            if t.title == title:
                self.tasks.remove(t)
                if self.storage:
                    self.storage.save(self.tasks)
                return
        raise ValueError("Task not found!")

    def mark_task_completed(self, title):
        for t in self.tasks:
            if t.title == title:
                t.mark_completed()
                if self.storage:
                    self.storage.save(self.tasks)
                return
        raise ValueError("Task not found!")

    def list_tasks(self):
        return self.tasks


class Storage:

    def save(self, tasks):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError


class JsonStorage(Storage):

    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def save(self, tasks):
        data = [task.to_dict() for task in tasks]  # Превращаем список объектов Task в список словарей
        with open(self.filename, "w", encoding="UTF-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load(self):
        try:
            with open(self.filename, "r", encoding="UTF-8") as f:
                data = json.load(f)
            tasks = []
            for item in data:
                task = Task(item['title'], item.get("description", ""))
                if item.get("completed", False):
                    task.mark_completed()
                tasks.append(task)
            return tasks
        except FileNotFoundError:
            return []


class Command:

    def execute(self):
        raise NotImplementedError


class AddTaskCommand(Command):

    def __init__(self, manager, task):
        self.manager = manager
        self.task = task

    def execute(self):
        self.manager.add_task(self.task)


class RemoveTaskCommand(Command):

    def __init__(self, manager, title):
        self.manager = manager
        self.title = title

    def execute(self):
        self.manager.remove_task(self.title)


class CompleteTaskCommand(Command):

    def __init__(self, manager, title):
        self.manager = manager
        self.title = title

    def execute(self):
        self.manager.mark_task_completed(self.title)


class TaskManagerApp:

    def __init__(self, manager):
        self.manager = manager

    def run_command(self, command):
        command.execute()

if __name__ == "__main__":
    storage = JsonStorage()
    manager = TaskManager(storage)
    app = TaskManagerApp(manager)

    # Создание команд
    add_cmd1 = AddTaskCommand(manager, Task("Сделать ДЗ", "по математике"))
    add_cmd2 = AddTaskCommand(manager, Task("Купить продукты", "молоко и хлеб"))

    complete_cmd = CompleteTaskCommand(manager, "Сделать ДЗ")
    remove_cmd = RemoveTaskCommand(manager, "Купить продукты")

    # Выполнение команд через Invoker
    app.run_command(add_cmd1)
    app.run_command(add_cmd2)
    app.run_command(complete_cmd)
    app.run_command(remove_cmd)

    # Печать всех задач
    for task in manager.list_tasks():
        print(task.to_dict())