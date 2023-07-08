from django.test import TestCase, Client

c = Client()

class SampleTest(TestCase):

    def setUp(self):
        print('All setUp done')

    def test_chencking_setup(self):
        print('well done')

    