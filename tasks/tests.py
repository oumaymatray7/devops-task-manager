from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task
from datetime import date

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='1234'
        )

        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            priority='High',
            status='Pending',
            due_date=date.today(),
            assigned_to=self.user
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.priority, 'High')
        self.assertEqual(self.task.status, 'Pending')