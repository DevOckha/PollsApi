from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from polls import views

class TestsPoll(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.uri = '/polls/'
        self.user = self.setup_user()
        self.view = views.PollViewSet.as_view({'get':'list'})
    
    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            username='test',
            email = 'testuser@gmail.com',
            password = 'test'
        )
    
    def _test_list(self):
        request = self.factory.get(self.uri)
        request.user = self.user
        response = self.view(request)

        self.assertEqual(response.status_code, 200)
