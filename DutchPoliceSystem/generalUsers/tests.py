from django.test import SimpleTestCase,TestCase,Client
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from generalUsers.views import userDash, registerPage,loginPage,logoutUser, index

# Create your tests here.
#Class for General User users to test URLs 
class TestUrl(SimpleTestCase):
    #General User Dashboard URL
    def test_userDash_url_is_resolved(self):
        url = reverse('userDash')
        self.assertEquals(resolve(url).func,userDash)
    #General User Register URL
    def test_registerUser_url_is_resolved(self):
        url = reverse('registerUser')
        self.assertEquals(resolve(url).func,registerPage)
    #General User Login URL
    def test_loginUser_url_is_resolved(self):
        url = reverse('loginUser')
        self.assertEquals(resolve(url).func,loginPage)
    #General User logout URL
    def test_logoutUser_url_is_resolved(self):
        url = reverse('logoutUser')
        self.assertEquals(resolve(url).func,logoutUser)
   
