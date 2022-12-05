from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadDataForm
from .models import UploadDataModel

# Create your views here.

def createMessage(request):
    if request.method == 'POST':
        form = UploadDataForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is uploaded')
    else:
        form = UploadDataForm()
        context = {
            'form':form,
        }
    return render(request, 'datafiles/DataUpload.html', context)


#display all messages from user
def allUserList(request):
    messageList = UploadDataModel.objects.all()#select * from uploadDataModel
    context={'list':messageList}
    return render(request,'policeUsers/allMessages.html',context)
