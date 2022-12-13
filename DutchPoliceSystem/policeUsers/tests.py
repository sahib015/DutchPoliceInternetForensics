from django.test import SimpleTestCase,TestCase,Client

from django.contrib.auth.models import User
from django.urls import reverse, resolve
from policeUsers.views import home, registerPage,loginPage,logoutUser
from userNotifications.views import allUserList
from .forms import CreateRegistrationForm

#Class for Police users to test URLs 
class TestUrl(SimpleTestCase):
    #Police Dashboard URL
    def test_policeDash_url_is_resolved(self):
        url = reverse('policeDash')
        self.assertEquals(resolve(url).func,home)
    #Police Register URL
    def test_registerPolice_url_is_resolved(self):
        url = reverse('registerPolice')
        self.assertEquals(resolve(url).func,registerPage)
    #Police Login URL
    def test_loginPolice_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func,loginPage)
    #Police logout URL
    def test_logoutPolice_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func,logoutUser)
    #Police allMessages URL
    def test_allMessages_url_is_resolved(self):
        url = reverse('allMessages')
        self.assertEquals(resolve(url).func,allUserList)

# test login functionality
class LoginTest(TestCase):
    def setUp (self):
        self.loginPoliceUrl = reverse('login')
        self.user = User.objects.create_user(
            username='testUser',
            email='testUser@test.com',
            first_name='Test',
            last_name='User',
            password='userTest_01'
        )   
    # test for police login success
    def test_policeLogin_success(self):
       client = Client()
       response = client.post(self.loginPoliceUrl,{'username':'testUser','password':'userTest_01'},format='text/html')
       self.assertEqual(response.status_code, 302)
    # test for police unsuccessful login
    def test_policeLogin_fail(self):
       client = Client()
       response = client.post(self.loginPoliceUrl,{'username':'testUser','password':'userTest_021'},format='text/html')
       self.assertEqual(response.status_code, 200)

class TestForms(TestCase):
    def setUp(self):
        self.form_test_valid_data={
            'username':'policeTestUser',
            'first_name': 'police',
            'last_name':'test',
            'email': 'policetest@test.com',
            'password1': 'test_pol@123',
            'password2':'test_pol@123'
        }
        self.form_test_invalid_data={
            'username':'user3',
            'first_name': 'user',
            'last_name':'3',
            'email': 'user3@test.com',
            'password1': 'donkey123',
            'password2':'donkey@123'
        }
    #test for valid data in the form
    def test_createPoliceUser_valid(self):
        regForm= CreateRegistrationForm(data=self.form_test_valid_data)
        self.assertTrue(regForm.is_valid())

    #test for invalid data in the form
    def test_createPoliceUser_invalid(self):
        regForm= CreateRegistrationForm(data=self.form_test_invalid_data)
        self.assertFalse(regForm.is_valid())