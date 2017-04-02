from unittest import TestCase

from selenium import webdriver

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Safari()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000/polls')
        self.assertIn('Busco Ayuda', self.browser.title)