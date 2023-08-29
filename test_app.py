import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Block Sport', response.data)

    def test_prediction(self):
        response = self.app.post('/predict', data={'team1': 'TeamA', 'team2': 'TeamB'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Prediction:', response.data)

    def test_prediction_form(self):
        response = self.app.get('/')
        self.assertIn(b'<form action="/predict" method="post">', response.data)
        self.assertIn(b'Team 1:', response.data)
        self.assertIn(b'Team 2:', response.data)
        self.assertIn(b'<input type="submit" value="Predict">', response.data)

    def test_valid_prediction(self):
        response = self.app.post('/predict', data={'team1': 'TeamA', 'team2': 'TeamB'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Prediction:', response.data)

    def test_invalid_prediction(self):
        response = self.app.post('/predict', data={'team1': '', 'team2': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Prediction:', response.data)  # Expecting error handling message

    def test_nonexistent_route(self):
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Not Found', response.data)

if __name__ == '__main__':
    unittest.main()
