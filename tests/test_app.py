class TestBase(TestCase):

    def create_app(self):
    # Pass in configurations for tests

    def setUp(self):

    #  Will be called before every test

    def tearDown(self):

    #   Will be called after every test

    class TestViews(TestBase):

    def test_home_get(self):

        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)