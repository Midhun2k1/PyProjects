from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.http import HttpResponse

from .form import FormSubmissionForm
from .models import Department, Course, Material, FormSubmission


# Create your views here.
def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('SchoolApp:form')
        else:
            messages.info(request, 'Invalid Id')
            return redirect('SchoolApp:login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is taken")
                return redirect('SchoolApp:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print("User Created")
                return redirect('SchoolApp:login')
        else:
            messages.info(request, "Password is NOT MATCHING")
            return redirect('SchoolApp:register')
        messages.info(request, "User Created SUCCESSFULLY")
        return redirect('/')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def form_submission(request):
    form1 = FormSubmission.objects.all()
    courses = Course.objects.all()
    department_map = {}
    for course in courses:
        try:
            department_map[course.department].append(course)
        except KeyError:
            department_map[course.department] = [course]
    print(request.POST.get('materials_provided',''))
    if request.method == 'POST':
        print(request.POST.get('dob'))
        name = request.POST.get('name', '')
        dob = request.POST.get('dob', '')
        age = request.POST.get('age', '')
        gender = request.POST.get('gender', '')
        phone_number = request.POST.get('phone_number', '')
        mail_id = request.POST.get('mail_id', '')
        address = request.POST.get('address', '')
        department = Department.objects.filter(name=request.POST.get('department', ''))[0]
        course = Course.objects.filter(name=request.POST.get('course', ''))[0]
        purpose = request.POST.get('purpose', '')
        materials_provided = Material.objects.filter(name__in=request.POST.getlist('materials_provided', ''))
        form = FormSubmission(name=name,
                              dob=dob,
                              age=age,
                              gender=gender,
                              phone_number=phone_number,
                              mail_id=mail_id,
                              address=address,
                              department=department,
                              course=course,
                              purpose=purpose,)
        print(materials_provided)
        form.save()

        form.materials_provided.set(list(materials_provided))
        messages.info(request, 'Order Confirmed')
        return redirect('SchoolApp:form')

        # return HttpResponse("Order Confirmed. <a href='/'>Return to Home</a>")
    return render(request, 'form.html', {'form1': form1, 'department_map': department_map, 'materials': Material.objects.all()})
