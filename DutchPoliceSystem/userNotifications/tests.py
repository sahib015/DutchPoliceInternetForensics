from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse, resolve
from userNotifications.views import createMessage
from userNotifications.models import CreateNewMessage
from .forms import CreateNewMessageFrom

# Create your tests here.
#Class for user notifications to test URLs 
class TestUrl(SimpleTestCase):
    #General User Dashboard URL
    def test_addmessage_url_is_resolved(self):
        url = reverse('addMessage')
        self.assertEquals(resolve(url).func,createMessage)


