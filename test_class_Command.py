import unittest
from main import Task, TaskManager
from main import AddTaskCommand, RemoveTaskCommand, CompleteTaskCommand, TaskManagerApp


class TestCommands(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager(storage=None)  # Используем TaskManager без файла для тестов
        self.app = TaskManagerApp(self.manager)

    def test_add_task_command(self):
        task = Task("Сделать ДЗ")
        cmd = AddTaskCommand(self.manager, task)
        self.app.run_command(cmd)
        self.assertIn(task, self.manager.tasks)
        self.assertEqual(self.manager.tasks[0].title, "Сделать ДЗ")

    def test_remove_task_command(self):
        task = Task("Купить продукты")
        self.manager.add_task(task)
        cmd = RemoveTaskCommand(self.manager, "Купить продукты")
        self.app.run_command(cmd)
        self.assertNotIn(task, self.manager.tasks)

        # Проверяем удаление несуществующей задачи
        cmd2 = RemoveTaskCommand(self.manager, "Несуществующая")
        with self.assertRaises(ValueError):
            self.app.run_command(cmd2)

    def test_complete_task_command(self):
        task = Task("Почитать книгу")
        self.manager.add_task(task)
        cmd = CompleteTaskCommand(self.manager, "Почитать книгу")
        self.app.run_command(cmd)
        self.assertTrue(task.completed)

        # Проверяем отметку несуществующей задачи
        cmd2 = CompleteTaskCommand(self.manager, "Несуществующая")
        with self.assertRaises(ValueError):
            self.app.run_command(cmd2)


if __name__ == '__main__':
    unittest.main()
