from django.test import SimpleTestCase
from django.urls import reverse, resolve
from policeUsers.views import home, registerPage,loginPage,logoutUser

#Class for Police users to test URLs 
class TestUrl(SimpleTestCase):
    def test_policeDash_url_is_resolved(self):
        url = reverse('policeDash')
        self.assertEquals(resolve(url).func,home)

    def test_registerPolice_url_is_resolved(self):
        url = reverse('registerPolice')
        self.assertEquals(resolve(url).func,registerPage)

    def test_loginPolice_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func,loginPage)

    def test_logoutPolice_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func,logoutUser)