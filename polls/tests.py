from django.test import TestCase
from django.utils import timezone
from polls.models import Question  # Explicit import


class QuestionTests(TestCase):
    def test_recent_publication(self):
        """Test was_published_recently()"""
        q = Question(pub_date=timezone.now())
        self.assertTrue(q.was_published_recently())


# 👇 Ensure this is the last line (empty newline)
