import unittest


class MyTestCase(unittest.TestCase):
    def test_add_task(self):
        from main import Task, TaskManager
        manager = TaskManager()
        task = Task("Почитать книгу", "30 минут перед сном")
        manager.add_task(task)

        # Проверяем, что список задач содержит нашу задачу
        self.assertIn(task, manager.tasks)

        # Проверяем, что название задачи совпадает
        self.assertEqual(manager.tasks[0].title, "Почитать книгу")


if __name__ == '__main__':
    unittest.main()
