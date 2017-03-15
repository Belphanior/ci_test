from django.test import TestCase

# Create your tests here.

class MyTest(TestCase):
    def test_equal(self):
        self.assertEqual(1,1)