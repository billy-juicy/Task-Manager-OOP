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

    def test_remove_task(self):
        from main import Task, TaskManager
        manager = TaskManager()
        task = Task("Почитать книгу")
        manager.add_task(task)
        manager.remove_task("Почитать книгу")

        # Удаляем задачу
        self.assertNotIn(task, manager.tasks)

        # Попытка удалить несуществуюущую задачу
        with self.assertRaises(ValueError):
            manager.remove_task("Несуществующая задача")

    def test_mark_task_completed(self):
        from main import Task, TaskManager
        manager = TaskManager()
        task = Task("Почитать книгу")
        manager.add_task(task)

        # Отмечаем задачу как выполненную
        manager.mark_task_completed("Почитать книгу")
        self.assertTrue(task.completed)

        # Попытка отметить несуществующую задачу
        with self.assertRaises(ValueError):
            manager.mark_task_completed("Несуществующая задача")

if __name__ == '__main__':
    unittest.main()
