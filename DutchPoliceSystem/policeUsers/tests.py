from django.test import SimpleTestCase,TestCase,Client

from django.contrib.auth.models import User
from django.urls import reverse, resolve
from policeUsers.views import home, registerPage,loginPage,logoutUser
from userNotifications.views import allUserList

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


class TestView(TestCase):
    def setUp (self):
        self.loginPoliceUrl = reverse('login')
        self.user = User.objects.create_user(
            username='testUser',
            email='testUser@test.com',
            first_name='Test',
            last_name='User',
            password='userTest_01'
        )   
    def test_policeLogin_success(self):
       client = Client()
       response = client.post(self.loginPoliceUrl,{'username':'testUser','password':'userTest_01'},format='text/html')
       self.assertEqual(response.status_code, 302)

    def test_policeLogin_fail(self):
       client = Client()
       response = client.post(self.loginPoliceUrl,{'username':'testUser','password':'userTest_021'},format='text/html')
       self.assertEqual(response.status_code, 200)