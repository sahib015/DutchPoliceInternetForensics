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


class TestForms(TestCase):
    def setUp(self):
        #dummy test values for valid data
        self.form_test_valid_data= {
            'date':'12/12/2022',
            'name': 'user1',
            'email': 'user1@test.com',
            'content': 'This is a test message for testing purposes',
            'levelOfPriority':'Low'
        }
        #dummy test values for invalid data
        self.form_test_invalid_data= {
            'date':'12/12/2022',
            'name': 'user1',
            'email': 'user1@test.com',
            'content': 'This is a test message for testing purposes',
            'levelOfPriority':'low'
        }
    #test for valid data in the form
    def test_createMessage_valid(self):
        newForm= CreateNewMessageFrom(data=self.form_test_valid_data)
        self.assertTrue(newForm.is_valid())
    #test for invalid data in the form
    def test_createMessage_invalid(self):
        newForm= CreateNewMessageFrom(data=self.form_test_invalid_data)
      
        self.assertFalse(newForm.is_valid())
        