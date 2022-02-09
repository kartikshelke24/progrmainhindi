
from django.http.response import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

from home.models import Contact

# Create your views here.
def index(request):
    
    return render(request, 'home/index.html')
    
def contact(request):
    if User.is_authenticated:
        if request.method=="POST":
            name=request.POST['name']
            email=request.POST['email']
            phone_num=request.POST['phone_num']
            message =request.POST['message']
            contact=Contact(name=name, email=email, phone_num=phone_num, message=message)
            contact.save()
            messages.success(request, {'msg':"Your message is sent successfully",'title':"Hello"},extra_tags="simple_tag")

        return render(request, 'home/contact.html')
    else:
        messages.warning(request, "")
       
    


def loginForm(request):
    if request.method == 'POST':
        your_email = request.POST.get('your_email')
        password = request.POST.get('your_pass')
        # username = User.objects.get(email=your_email.lower()).username
        # userFirstName = User.objects.get(email=your_email.lower()).first_name
      
        data = {}
        data["emailVal"] = your_email
        data["passwordVal"] = password
        try:
            username = User.objects.get(email=your_email.lower()).username
            allClear = False
        except:
            data["email"] = "Email is not rigestered"
            return render(request,'home/login.html',data)


        # only email valid 
        # password is remaining 




        user = authenticate(username=username,password=password)
        if not user:
            data["password"] = "Password is incorrect"
            return render(request,'home/login.html',data)

        if user is not None:    
            login(request,user)
            messages.success(request, "Login Successful", extra_tags="simple_tag")    
            return redirect('index')

        else:
            return redirect('loginForm')
    
    return render(request, 'home/login.html')
    
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['your_name']
        email = request.POST['your_email']
        password = request.POST['your_pass']
        cpassword = request.POST['confirm_your_pass']
       
        allClear = True
        data= {} 
        
        if len(username)<3:
            data["username"] = "username min 3 charcter"
            allClear = False      

        elif len(username)>15:
            data["username"] = "username max 15 charcter"
            allClear = False      

        elif not(username.isalnum()):
            data["username"] = "username contains only alphabates & numbers"
            allClear = False

        try:
            checks_User = User.objects.get(username=username)
            data["username"] = "username already taken"
            allClear = False
        except:
            pass
        try:
            checks_Email = User.objects.get(email=email)
            data["email"] = "email already register"
            allClear = False
        except:
            pass

        if len(name)<3:
            data["name"] = "name min 3 charcter"
            allClear = False
        
        elif not(name.isalpha()):
            data["name"] = "name contains only alphabates"
            allClear = False
        
        if len(password)<5:
            data["password"] = "password min 6 charcter"
            allClear = False
       
        if not(password==cpassword):
            data["cpassword"] = "password  is not matching"
            allClear = False
        
        data["usernameVal"] = username
        data["nameVal"] = name
        data["emailVal"] = email
        data["passwordVal"] = password
        if not (allClear):
            return render(request,'home/signup.html',data)
        if allClear:
            # Creating user
            myuser = User.objects.create_user(username,email,password)
            myuser.first_name = name
            myuser.save()
            messages.success(request,"Registration SucessFull",extra_tags="simple_tag")
            return redirect('loginForm')
        
        # return render(request,'home/signup.html',data)
    return render(request, 'home/signup.html')
    
def logoutHandle(request):
    a = messages.success(request,"Logout Successful",extra_tags="logout_tags")
    print(a)
    logout(request)
    return redirect('index')

