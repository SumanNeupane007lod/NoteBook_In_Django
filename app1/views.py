from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .forms import Bookform
from .models import Book
# Create your views here.
def home(request):
    context={}
    if request.method == 'POST':
        uploaded_file = request.FILES['Document']
        fs = FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        context['url']=fs.url(name)
        
    return render(request,'app1/home.html',context)


def booklist(request):
    notes=Book.objects.all()
    return render(request,'app1/book_list.html',{'notes':notes})

def bookupload(request):
    if request.method=='POST':
        form=Bookform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('booklist')
    else:
        form=Bookform()
    return render(request,'app1/book_upload.html',{'form':form})
def aboutus(request):
    return render(request,'app1/Aboutus.html')