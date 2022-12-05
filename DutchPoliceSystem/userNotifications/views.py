from django.shortcuts import render,redirect
from django.contrib import messages

from cryptography.fernet import Fernet
from .forms import UploadDataForm,CreateNewMessageFrom
from .models import UploadDataModel,CreateNewMessage


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

        #generate the key to be used for encryption and decryption
        key = Fernet.generate_key()
 
        # Instance the Fernet class with the key
 
        fernet = Fernet(key)

        #encrypt the message
        encMessage = fernet.encrypt(contentMsg.encode())

        #check if the form is valid before saving to the database
        if addMsgForm.is_valid():
             #encrypt the message
            encMessage = fernet.encrypt(contentMsg.encode())
            addMsgForm.content = encMessage
            addMsgForm.save('content') #save details to the database
            addMsgForm.save() #save details to the database
            print("content: "+contentMsg)
            print(encMessage)

            #pass messages to the dashboard
            messages.success(request,'your message has been recieved and we shall respond within 72 hours')

            return redirect('userDash') #redirects user to the user dashboard
    context = {'form':addMsgForm}
    return render(request,'datafiles/DataUpload.html',context)#renders the register page with context details 

#display all messages from user
def allUserList(request):
    data = CreateNewMessage.objects.all()#select * from createnewmessage
    context={'msgs':data}
    return render(request,'policeUsers/allMessages.html',context)
