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

#calss for testing the views


    
class TestForm(SimpleTestCase):
    def test_new_message_form_valid_data(self):
        form = CreateNewMessageFrom(data={
            'date':12/12/2022,
            'name':"user01",
            'email':"user01@test.com",
            'content':"this is a dummy test description for testing purposes",
            'levelOfPriority':"low"
        })
        self.assertTrue(form.is_valid())

    def test_new_message_form_invalid_data(self):
        newMessageForm = CreateNewMessageFrom(data={})
        self.assertFalse(newMessageForm.is_valid())
        self.assertEqual(len(newMessageForm.errors),5)
