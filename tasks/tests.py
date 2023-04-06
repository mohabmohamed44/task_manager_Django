from django.test import TestCase
from django.urls import reverse
from .models import Task


class TaskModelTests(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(title='Test task')
        self.assertEqual(task.title, 'Test task')


class TaskIndexViewTests(TestCase):
    def test_no_tasks(self):
        response = self.client.get(reverse('task_manager:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No tasks are available.')
        self.assertQuerysetEqual(response.context['latest_task_list'], [])

    def test_one_task(self):
        task = Task.objects.create(title='Test task')
        response = self.client.get(reverse('task_manager:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, task.title)
        self.assertQuerysetEqual(
            response.context['latest_task_list'],
            ['<Task: Test task>']
        )
