from django.test import SimpleTestCase,TestCase,Client
from django.contrib.auth import get_user
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

