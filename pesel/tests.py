from django.test import TestCase
from django.urls import reverse


class PeselViewTest(TestCase):

    def test_invalid_pesel_format(self):
        response = self.client.post(reverse('pesel:pesel'), {'pesel': '12345'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PESEL must be an 11-digit number.')

    def test_invalid_pesel_control_digit(self):
        response = self.client.post(reverse('pesel:pesel'), {'pesel': '12345678902'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid PESEL number')

    def test_get_request(self):
        response = self.client.get(reverse('pesel:pesel'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pesel/pesel.html')