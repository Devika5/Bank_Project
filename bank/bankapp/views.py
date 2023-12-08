from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth

from bankapp.models import District, Branchs, Account, Material

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        password2 = request.POST.get('pass2')


        if not username or not password:
            messages.error(request, "Please provide a username and password.")
            return redirect('register')

        if password != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        try:
            # Check if the user already exists
            existing_user = User.objects.get(username=username)
            messages.error(request, "Username is already taken.")
            return redirect('register')
        except User.DoesNotExist:
            # Create a new user
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "User created successfully.")
            return redirect('login')  # Create this view and template

    return render(request, 'register.html')




def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('new')
        else:
            messages.info(request,"Invalid username or password")
            return redirect('login')

    return render(request,'login.html')




def new(request):
    return render(request,'new.html')


def form(request):
    selected_district_id = request.GET.get('district')
    districts = District.objects.all()
    branches = {
        district.name: list(Branchs.objects.filter(district=district).values('id', 'name'))
        for district in districts
    }

    accounts = Account.objects.all()
    materials=Material.objects.all()
    return render(request, 'form.html',{'districts': districts, 'branches': branches, 'accounts': accounts, 'materials': materials})


def index(request):
    districts = District.objects.all()
    return render(request, 'index.html', {'districts': districts})

# def wikipedia(request):
#     return render(request, 'index.html')