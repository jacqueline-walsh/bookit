from django.test import TestCase, Client


# # Create your tests here.
class TestHomeView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_loaded_templates(self):
        response = self.client.get('/')
        templates = response.templates
        names = get_names(templates)

        self.assertIn('base.html', str(names))
        self.assertIn('pages/index.html', str(names))
        self.assertIn('partials/_topbar.html', str(names))
        self.assertIn('partials/_navbar.html', str(names))
        self.assertIn('partials/_footer.html', str(names))

class TestAboutView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_loaded_templates(self):
        response = self.client.get('/about/')
        templates = response.templates
        names = get_names(templates)

        self.assertIn('base.html', str(names))
        self.assertIn('pages/about.html', str(names))
        self.assertIn('partials/_topbar.html', str(names))
        self.assertIn('partials/_navbar.html', str(names))
        self.assertIn('partials/_footer.html', str(names))

# Helper functions
def get_names(templates):
    names = []
    for t in templates:
        names.append(t.name)
    return names
