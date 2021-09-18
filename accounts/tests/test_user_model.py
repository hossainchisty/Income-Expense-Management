from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


class SigninTestCase(TestCase):

    def setUp(self):
        '''Test module for user model'''
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        '''Delete test user'''
        self.user.delete()

    def test_user_string_representation(self):
        '''Test user string representation'''
        self.assertEqual(str(self.user), self.user.username)

    def test_correct(self):
        '''Test correct username and password'''
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        '''Test wrong username'''
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        '''Test wrong password'''
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
