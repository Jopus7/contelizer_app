from django.test import TestCase
from django.urls import reverse


class FileUploadViewTest(TestCase):
    def test_file_upload(self):
        with open('test_file.txt', 'w') as test_file:
            test_file.write('Test content')
        with open('test_file.txt', 'rb') as test_file:
            response = self.client.post(reverse('files:file_upload'), {'file': test_file})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'texts/display.html')

    def test_invalid_file_upload(self):
        response = self.client.post(reverse('files:file_upload'), {})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'texts/upload.html')
        self.assertContains(response, 'This field is required.')

    def test_valid_file_shuffling(self):
        with open('test_file.txt', 'w') as test_file:
            test_file.write('This is a test.')
        with open('test_file.txt', 'rb') as test_file:
            response = self.client.post(reverse('files:file_upload'), {'file': test_file})
        shuffled_content = response.context['name']
        self.assertNotEqual(shuffled_content, 'This is a test.')

    def test_single_word_upload(self):
        with open('single_word_file.txt', 'w') as single_word_file:
            single_word_file.write('Single')

        with open('single_word_file.txt', 'rb') as single_word_file:
            response = self.client.post(reverse('files:file_upload'), {'file': single_word_file})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'texts/display.html')