# Just like the main Flask app, we're going to do some imports
# First, because we're writing tests for the Flask app inside
# web_starter, we'll need to import it
from web_starter.app import app

# Now we're going to import the TestCase class from Flask.ext.testing
from flask.ext.testing import TestCase

# Finally, we'll import the popular unittest framework
import unittest


class WebStarterTest(unittest.TestCase):

    def test_homepage(self):
        """ Tests the homepage method """
        # Create a test variable
        tester = app.test_client(self)
        # Get the page at "/"
        response = tester.get('/')
        # Assert the response code of the page at "/" is 200 (successful)
        self.assertEqual(response.status_code, 200)
        # Assert the content of the page at "/" shows "Hello World"
        self.assertEqual(response.data, "Hello World")

    def test_basic_page(self):
        """ Tests the basic-page method """
        # Create a test variable
        tester = app.test_client(self)
        # Get the page at "/basic-page/"
        response = tester.get('/basic-page/', content_type='html/text')
        # Assert the response code of the page at "/basic-page"
        # is 200 (successful)
        self.assertEqual(response.status_code, 200)
        # Assert the content of the page at "/basic-page" shows "Isn't it
        # sweet"
        self.assertTrue("Isn't it sweet" in response.data)

    def test_dynamic_page_no_args(self):
        """ Tests the dynamic-page method with NO args """
        # Create a test variable
        tester = app.test_client(self)
        # Get the page at "/dynamic-page/"
        response = tester.get('/dynamic-page/', content_type='html/text')
        # Assert the response code of the page at "/dynamic-page/" is 200
        # (successful)
        self.assertEqual(response.status_code, 200)
        # Assert the response code of the page at "/dynamic-page/" shows
        # "Add some query arguments"
        self.assertTrue("Add some query arguments" in response.data)

if __name__ == "__main__":
    unittest.main()
