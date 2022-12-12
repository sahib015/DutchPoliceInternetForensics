from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse, resolve
from userNotifications.views import createMessage
from userNotifications.models import CreateNewMessage

# Create your tests here.
#Class for user notifications to test URLs 
class TestUrl(SimpleTestCase):
    #General User Dashboard URL
    def test_addmessage_url_is_resolved(self):
        url = reverse('addMessage')
        self.assertEquals(resolve(url).func,createMessage)

#calss for testing the views

class TestView(TestCase):
    def setup(self):
        self.client = Client()
      

    def test_createNewMessage_post(self):
     
        response = self.client.post(reverse('addMessage'),{
            'date': '12/12/2022',
            'name': 'user1',
            'email': 'user1@test.com',
            'content': 'this is a dummy test description for testing puroposes',
            'levelOfPriority': 'low'
        })
        self.assertEquals(response.status_code,200)
        