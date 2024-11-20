from django.test import TestCase, Client


class TestingStageDemo(TestCase):
    def setUp(self):
        self.a = 1
        self.b = 2

    def test_sum(self):
        self.assertEqual(self.a + self.b, 3)


class TestingStageDemo2(TestCase):
    def setUp(self):
        self.c = Client()

    def test_request(self):
        response = self.c.get("/api2/")
        self.assertEqual(response.status_code, 200)