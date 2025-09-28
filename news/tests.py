from django.test import TestCase
from .models import PostModel
from django.urls import reverse


# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        PostModel.objects.create(title='test', text='test')

    def test_text_content(self):
        post = PostModel.objects.get(id=1)
        expected_object_title = f'{post.title}'
        expected_object_text = f'{post.text}'
        self.assertEqual(expected_object_title, 'test')
        self.assertEqual(expected_object_text, 'test')


class NewsViewTest(TestCase):
    def setUp(self):
        PostModel.objects.create(title='test', text='test')

    def test_views_url(self):
        res = self.client.get("")
        self.assertEqual(res.status_code, 200)

    def test_view_url_by_name(self):
        res = self.client.get(reverse("home page"))
        self.assertEqual(res.status_code, 200)

    def test_view_uses_correct_template(self):
        res = self.client.get(reverse("home page"))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home.html')
