from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadDataForm

# Create your views here.

def DataUploadView(request):
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
