from django.shortcuts import render,redirect
from django.contrib import messages

# Import encryption library
from cryptography.fernet import Fernet

# Import RSA public-key cryptosystem library
import rsa
# Import variablies from forms.py
from .forms import CreateNewMessageFrom

# Import variablies from models.py
from .models import CreateNewMessage

# declare private variables
#generate the key to be used for encryption and decryption
#key = Fernet.generate_key()
key = "JlmWZv4MSbQ34Kw26xNlW7iZaqz0U6HOeez_Ucq-ijQ="
# Instance the Fernet class with the key
fernet = Fernet(key)

# Public Key and Private Key generation
publicKey, privateKey = rsa.newkeys(512)

# Create your views here.
def createMessage(request):
    print (key)
    addMsgForm = CreateNewMessageFrom()
    #store data into the databse
    if request.method=="POST":
        addMsgForm= CreateNewMessageFrom(request.POST)

        # encryption of the content message below
        contentMsg = request.POST.get('content')
        if addMsgForm.is_valid():
            #encrypt the message
            #fernet.encrypt(contentMsg.encode())
            encMessage = rsa.encrypt(contentMsg.encode(),publicKey)
            decMessage = rsa.decrypt(encMessage, privateKey).decode()

            #save details to the database
            addMsgForm.save()

            print("content: "+contentMsg)

            print(encMessage)
            print("decoded: "+ decMessage)

            # update content message and store the encoded message in the database
            lastRecord(encMessage)
            #pass messages to the dashboard
            messages.success(request,'your message has been recieved and we shall respond within 72 hours')

            #redirects user to the user dashboard
            return redirect('userDash')
    context = {'form':addMsgForm}

    #renders the register page with context details
    return render(request,'datafiles/DataUpload.html',context)

#display all messages from user
def allUserList(request):
    #select * from createnewmessage
    data = CreateNewMessage.objects.all()
    description = CreateNewMessage.objects.values('content')

    print("Content from DB: "+str(description))

    # for content in description:
    # print(content)
    # decMessage = rsa.decrypt(content, privateKey).decode()
    # print("decrypted string: ", decMessage)

    context={'msgs':data}
    return render(request,'policeUsers/allMessages.html',context)

#get last record added to the database
def lastRecord(encodeMsg):
    message_obj = CreateNewMessage.objects.get(id=CreateNewMessage.objects.last().id)
    message_obj.content= encodeMsg
    message_obj.save()
