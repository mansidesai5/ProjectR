from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        empID = request.POST['empID'],
        Name = request.POST['Name'],
        designation = request.POST['designation'],
        department = request.POST['department'],
        password = request.POST['password'],
        password2 = request.POST['password2'],
        
        
        
        if password == password2:
            if User.objects.filter(empID= empID).exists():
                # messages.info(request,'Email is already registered')
                return redirect('register')
            elif User.objects.filter(Name=Name).exists():
                # messages.info(request,'Username is already used')
                return redirect('register')
            else:
                user = User.objects.create_user(Name=Name, empID=empID, password=password)
                user.save()
                return redirect('/')
        
        # Checking if the passwords match
        if password == password2:
            if User.objects.filter(empID=empID).exists():
                return redirect('register', {'error':'This employee ID is already in use.'})
            elif User.objects.filter(Name=Name).exists():
                return redirect('register', {'error':'This name is already registered.'})
            else:
                user = User(empID=empID, Name=Name, designation=designation, department=department)
                user.set_password(password)
                user.save()
                
                return redirect('/')
        else:
            return render(request, 'register.html')            
            
    return render(request,'register.html')                
    
def login(request):
    error = ''
    if request.method == "POST":
        empID = request.POST["empID"],
        password = request.POST["password"]
        user = auth.authenticate(username=empID, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            error = "Invalid Employee ID or Password"
    
    return render(request,"/",{"error":error})           

# @login_required
# def dashboard(request):
#     context={}
#     # Get the current logged-in user
#     user = request.user

#     # Retrieve all tasks for     this user and sort them by due date (latest first)
#     tasks = Task.objects.filter(owner=user).order_by('dueDate','completed')

#     # Calculate how many tasks are overdue
#     overDue = tasks.filter(dueDate__lt=timezone.now()).count()
        
# def login(request):
#     return render(request,'login.html')
    