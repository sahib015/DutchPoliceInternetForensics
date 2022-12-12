from django.test import SimpleTestCase,TestCase,Client
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from generalUsers.views import userDash, registerPage,loginPageUser,logoutUser, index

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
        self.assertEquals(resolve(url).func,loginPageUser)
    #General User logout URL
    def test_logoutUser_url_is_resolved(self):
        url = reverse('logoutUser')
        self.assertEquals(resolve(url).func,logoutUser)
   
class TestView(TestCase):
    def setUp (self):
        self.loginUserUrl = reverse('loginUser')
        self.user = obj1 = User.objects.create_user(
        username='testUser2',
        email='testUser2@test.com',
        first_name='test',
        last_name='user2',
        password='TestUser_02'
    )
     # test for user login successfull    
    def test_userLogin_success(self):
       client2 = Client()
       response = client2.post(self.loginUserUrl,{'username':'testUser2','password':'TestUser_02'},format='text/html')
       self.assertEqual(response.status_code, 302)
    #test for user unscuccessful login
    def test_userLogin_fail(self):
       client2 = Client()
       response = client2.post(self.loginUserUrl,{'username':'testUser','password':'userTest_021'},format='text/html')
       self.assertEqual(response.status_code, 200)
