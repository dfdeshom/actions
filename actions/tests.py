from django.test import TestCase
from django.core.urlresolvers import reverse
from utils import create_random_action


class ActionsIndexViewTests(TestCase):

    def test_index_no_actions(self):
        response = self.client.get(reverse('actions:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No actions are available.")

    def test_index(self):
        create_random_action()
        response = self.client.get(reverse('actions:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<ul>")
        self.assertContains(response, "<li>")


class ActionsIndexMonthTests(TestCase):

    def test_no_actions(self):
        response = self.client.get(reverse('actions:thismonth'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No actions are available.")

    def test_no_actions_this_month(self):
        create_random_action(thismonth=False)
        response = self.client.get(reverse('actions:thismonth'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No actions are available.")

    def test_actions_this_month(self):
        create_random_action()
        response = self.client.get(reverse('actions:thismonth'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<ul>")
        self.assertContains(response, "<li>")
