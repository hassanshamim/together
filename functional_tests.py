from selenium import webdriver

import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_new_visitor_visits_site(self):

        # Yousuf has heard about my cool new online app.  He goes to check out its homepage

        # He notices the page title and header mention the app name
        self.assertIn('Together', self.browser.title)
        self.fail('Finish the test!')

        # He is invited to sign up.

        # He clicks the 'Sign up' link

        # He is taken to the SignUp page

        # He sees he can sign up via his Facebook account

        # He does so

        # He now sees 'Yousuf' on the page

        # He is happy for now, and goes and plays bass

if __name__ == '__main__':
    unittest.main(warnings='ignore')
