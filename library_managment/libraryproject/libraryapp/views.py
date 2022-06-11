from django.http import HttpResponse
from django.shortcuts import render
from .models import Admin
from .models import Book


# Create your views here.

def index(request):
    return render(request, 'libraryapp/index.html')


def adminloginform(request):
    return render(request, 'libraryapp/adminloginform.html')


def adminsigninform(request):
    return render(request, 'libraryapp/adminsigninform.html')


def admindata(request):
    vname = request.POST.get("textname")
    vphone = request.POST.get("phone")
    vemailid = request.POST.get("textmailid")
    vpassword = request.POST.get("password")
    adminobj = Admin(name=vname, phone=vphone, emailid=vemailid, password=vpassword, )
    adminobj.save()
    return HttpResponse("Admin  registerd")


def admin(request):
    emailid = request.POST.get('textmailid')
    password = request.POST.get('password')
    # store a data in session variable
    request.session['emailid'] = emailid
    request.session['password'] = password
    adminobj = Admin.Objects.get(emailid=emailid, password=password)
    return render(request, 'libraryapp/adminhome.html')


def adminhome(request):
    return render(request, 'libraryapp/adminhome.html')



def addbook(request):
    return render(request, 'libraryapp/addbook.html')


def bookupdate(request):
    vname = request.POST.get("bname")
    vauthorname = request.POST.get("aname")
    vbookprice = request.POST.get("bookprice")
    vbooklocation = request.POST.get("booklocation")
    bookobj = Book(bookname=vname, Authorname=vauthorname, bookprice=vbookprice, booklocation=vbooklocation, )
    bookobj.save()
    return HttpResponse("Book registerd")

def viewbook(request):
    bookobj = Book.Objects.all()
    return render(request, 'libraryapp/retrivevebook.html', {'bookobj': bookobj})


def updatebook(request,slug):
    bname = slug
    bookobj = Book.Objects.get( bookname=bname)
    return render(request, 'libraryapp/updatebook.html',{"bookobj": bookobj})


def ubook(request):
    vname = request.POST.get("bname")
    vauthorname = request.POST.get("aname")
    vbookprice = request.POST.get("bookprice")
    vbooklocation = request.POST.get("booklocation")
    bookobj = Book.Objects.get(bookname=vname)
    bookobj.Authorname=vauthorname
    bookobj.bookprice=vbookprice
    bookobj.booklocation=vbooklocation
    bookobj.save()
    return HttpResponse("Book Updated")



def studentbookview(request):
    bookobj = Book.Objects.all()
    return render(request, 'libraryapp/studentview.html', {'bookobj': bookobj})


def deletebook(request,slug):
    bname = slug
    bookobj = Book.Objects.get(bookname=bname)
    return render(request, 'libraryapp/deletebook.html', {"bookobj": bookobj})

def dbook(request):
    vname = request.POST.get("bname")
    bookobj = Book.Objects.get(bookname=vname)
    bookobj.delete()
    return HttpResponse("Book deleted")