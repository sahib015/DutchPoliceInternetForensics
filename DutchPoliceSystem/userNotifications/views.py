from django.shortcuts import render,redirect
from django.contrib import messages

from cryptography.fernet import Fernet
from .forms import UploadDataForm,CreateNewMessageFrom
from .models import UploadDataModel,CreateNewMessage

# declare private variables
#generate the key to be used for encryption and decryption
key = Fernet.generate_key()
# Instance the Fernet class with the key
fernet = Fernet(key)

# Create your views here.

def createMessage(request):
    """
    if request.method == 'POST':
        form = UploadDataForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is uploaded')
    else:
        newMsgForm = createNewMessageFrom()
        context = {
            'form':newMsgForm,
        }
    return render(request, 'datafiles/DataUpload.html', context)
    """
    addMsgForm = CreateNewMessageFrom()
    #store data into the databse
    if request.method=="POST":
        addMsgForm= CreateNewMessageFrom(request.POST)
        
        # encryption of the content message below
        contentMsg = request.POST.get('content')

       


        #check if the form is valid before saving to the database
        if addMsgForm.is_valid():
             #encrypt the message
            encMessage = fernet.encrypt(contentMsg.encode())
            
            addMsgForm.save() #save details to the database

            print("content: "+contentMsg)
            print(encMessage)
            lastRecord(encMessage) # update content message and store the encoded message in the database
            #pass messages to the dashboard
            messages.success(request,'your message has been recieved and we shall respond within 72 hours')

            return redirect('userDash') #redirects user to the user dashboard
    context = {'form':addMsgForm}
    return render(request,'datafiles/DataUpload.html',context)#renders the register page with context details 

#display all messages from user
def allUserList(request):
    data = CreateNewMessage.objects.all()#select * from createnewmessage
    #decMessage = fernet.decrypt(encMessage).decode()
 
    #print("decrypted string: ", decMessage)
    context={'msgs':data}
    return render(request,'policeUsers/allMessages.html',context)

#get last record added to the database
def lastRecord(encodeMsg):
    student_obj = CreateNewMessage.objects.get(id=CreateNewMessage.objects.last().id)
    student_obj.content= encodeMsg
    student_obj.save()