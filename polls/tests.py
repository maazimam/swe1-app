from django.test import TestCase
from .models import Question
from django.utils import timezone


class QuestionModelTests(TestCase):
    def test_was_published_recently(self):
        q = Question(pub_date=timezone.now())
        self.assertTrue(q.was_published_recently())
