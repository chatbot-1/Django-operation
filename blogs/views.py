from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):

    popularBlogs = Popular.objects.all()
    context = {
        'popularBlogs':popularBlogs
    }

    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def addBlog(request):
    return render(request, 'write.html')

def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email_add = request.POST['email_add']
        phone_num = request.POST['phone_num']
        address_data = request.POST['address_data']
        password_add = request.POST['password_add']
        message_here = request.POST['message_here']

        print(full_name, email_add, phone_num, address_data, password_add, message_here)

        # contactObj = ContactUs(
        #     full_name = full_name,
        #     emailadd = email_add,
        #     phonenum = phone_num,
        #     address = address_data,
        #     password = password_add,
        #     message = message_here,
        # )
        # contactObj.save()
    
    return render(request, 'contact.html')

def view_blog(request, pk):
    viewBlog = Popular.objects.get(pk = pk)
    return render(request, 'viewBlog.html', {'viewBlog':viewBlog})