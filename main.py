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

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        for t in self.tasks:
            if t.title == title:
                self.tasks.remove(t)
                return
        raise ValueError("Task not found!")

    def mark_task_completed(self, title):
        for t in self.tasks:
            if t.title == title:
                t.mark_completed()
                return
        raise ValueError("Task not found!")

    def list_tasks(self):
        return self.tasks


class Storage:

    def save(self, tasks):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError


t1 = Task("Сделать ДЗ", "по математике")
t2 = Task("Купить продукты", "молоко и хлеб")

manager = TaskManager()
manager.add_task(t1)
manager.add_task(t2)

for task in manager.list_tasks():
    print(task.to_dict())

manager.remove_task("Сделать ДЗ")

for task in manager.list_tasks():
    print(task.to_dict())

t3 = Task("Почитать книгу", "30 минут перед сном")
manager.add_task(t3)

manager.mark_task_completed("Почитать книгу")

for task in manager.list_tasks():
    print(task.to_dict())
