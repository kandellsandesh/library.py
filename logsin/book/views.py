from django.shortcuts import render,redirect
from . models import Book
from . forms import BookCreate
from django . http import HttpResponse

# Create your views here.
def home(request):
    transfer= Book.objects.all()
    return render(request,'lict.html',{'transfer':transfer})

def uploadform(request):
    upload= BookCreate()
    if request.method=='POST':
        upload=BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('home')
        else:
            return HttpResponse(""" something went wrong. wait for a minute """)
    else:
        return render(request,'uploadform.html',{'uploadform':upload})

def update_book(request,book_id):
    book_id= int(book_id)
    try:
        book_shelf=Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('home')
    book_form= BookCreate(request.POST or None, instance= book_shelf)    
    if book_form.is_valid():
        book_form.save()
        return redirect('home')
    return render(request,'uploadform.html',{'uploadform':book_form})

def delete_book(request,book_id):
    book_id=int (book_id)
    try:
        book_shelf=Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('home')
    book_shelf.delete()
    return redirect('home')




    


