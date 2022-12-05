from django.shortcuts import render,redirect
from django.contrib import messages
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
        #check if the form is valid before saving to the database
        if addMsgForm.is_valid():
            addMsgForm.save() #save details to the database
          

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
