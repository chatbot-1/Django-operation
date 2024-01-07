from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def home(request):

    popularBlogs = Popular.objects.all()
    regularBlogs = Regular_blogs.objects.all()

    return render(request, 'home.html', {'popularBlogs':popularBlogs, 'regularBlogs':regularBlogs})

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username!!')
            return redirect('/login/')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid/Incorrect Username or Password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('/')

def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.error(request, 'This username is already exist')
            return redirect('/signup/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        messages.info(request, 'Account created Successfulyy!!')
        return redirect('/login/')

    return render(request, 'signup.html')

def reset(request):
    if request.method == 'POST':
        name = request.POST['username']
        new_pass = request.POST['new_password']
        mat = User.objects.get(username = name)
        mat.set_password(new_pass)
        mat.save()
        messages.info(request, 'Password changed Successfulyy!!')
        return redirect('/login/')
    return render(request, 'reset.html')

def about(request):
    return render(request, 'about.html')

@login_required(login_url='/login/')
def addBlog(request):
    if request.method == 'POST':
        data = request.POST
        topic = data.get('topic')
        author = data.get('author')
        title = data.get('title')
        content = data.get('content')
        cover = request.FILES.get('cover')

        Regular_blogs.objects.create(
            topic = topic,
            author = author,
            title = title,
            content = content,
            cover = cover
        )
        return redirect('/')

    queryset = Regular_blogs.objects.all()
    context = {'regular':queryset}

    return render(request, 'write.html', context)

def contact(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        number = data.get('number')
        email = data.get('email')
        message = data.get('message')

        Contact.objects.create(
            name = name,
            number = number,
            email = email,
            message = message,
        )
    
    return render(request, 'contact.html')

def view_blog(request, pk):
    viewBlog = Popular.objects.get(pk = pk)
    return render(request, 'viewBlog.html', {'viewBlog':viewBlog})

def viewRegular(request, pk):
    viewRegularBlog = Regular_blogs.objects.get(pk = pk)
    return render(request, 'viewRegularBlogs.html', {'viewRegular':viewRegularBlog})
