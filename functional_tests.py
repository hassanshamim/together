from selenium import webdriver

import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_new_visitor_visits_site(self):

        # Yousuf has heard about my cool new online app.  He goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention the app name
        self.assertIn('Together', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Together', header_text)

        # He is invited to sign up.
        signup_link =  self.browser.find_elements_by_link_text('Sign Up')
        self.assertFalse(signup_link == [])

        self.fail('finish the test')
        # He clicks the 'Sign up' link

        # He is taken to the SignUp page

        # He sees he can sign up via his Facebook account

        # He does so

        # He now sees 'Yousuf' on the page

        # He is happy for now, and goes and plays bass

if __name__ == '__main__':
    unittest.main(warnings='ignore')
