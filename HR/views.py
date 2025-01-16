from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core import serializers
from django.db import IntegrityError, models
import json
from django.http import JsonResponse
from .models import User
from .models import User, employeestatus, task, todolist, leaves
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date, timedelta

# Create your views here.

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        image = request.FILES ["profileimage"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            userdata = employeestatus.objects.create(user = user, profileimage = image)
            
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "register.html")

def index(request):
    return render(request, "index.html")

def profile(request):
    return render(request, 'profile.html')

def home(request):
    user = request.user
    today = date.today()
    startdate = today -timedelta(days = today.weekday())
    enddate = startdate + timedelta(days =6)
    tasks = task.objects.filter(users = user, duedate__range = [startdate,enddate]).order_by('duedate')
    todos = todolist.objects.filter(user=user)
    return render(request, "home.html",
    {"tasks" : tasks,
    "todos" : todos,}
    )

def employees(request):
    employees = employeestatus.objects.all().order_by('-id')
    userinfo = employeestatus.objects.get(user = request.user)
    isboss = False
    if userinfo.role == 'Boss':
        isboss =True
    else:
        isboss =False
    return render (request, "employees.html",
    {"employees" : employees,
    "isboss": isboss}
    )

def remove_user(request,id):
    user = User.objects.get(pk = id)
    user.delete()
    return JsonResponse({
            "message": "user removed",
        })

def project (request):
    tasks = task.objects.filter(status = "Incomplete").order_by('duedate')
    employees = User.objects.all()
    user = request.user
    userinfo = employeestatus.objects.get(user = user)
    isboss = False
    if userinfo.role == 'Boss':
        isboss =True
    else:
        isboss =False
    return render(request, "projects.html",
    {"tasks" : tasks,
    "employees": employees,
    "isboss": isboss}
    )

def getprojects(request):
    # Query for requested data
    tasks = task.objects.filter(status = "Incomplete")
    task_serializers = serializers.serialize('json', tasks)
    return JsonResponse([task.serialize() for task in tasks], safe=False)

def addproject(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        duedate = request.POST ["duedate"]
        users_id = request.POST.getlist("employees")
        users = User.objects.filter(id__in = users_id)
        project = task.objects.create(title = title, description = description, duedate = duedate)
        project.save()
        for id in users_id:
            project.users.add(id)
        return HttpResponseRedirect(reverse("projects"))

def markasdone(request,id):
        project = task.objects.get(pk = id)
        project.status = "Complete"
        project.save()
        return JsonResponse({
            "message": "project complete",
            "project": project.title,
        })
def addtodo(request, todovalue):
    user = request.user
    x = todolist.objects.create(user = user, todoitem = todovalue)
    x.save()
    return JsonResponse({
            "message": "item added",
            "item": x.todoitem,
        })

def removetodo(request, id):
    user = request.user
    x = todolist.objects.get(pk = id)
    x.delete()
    return JsonResponse({
            "message": "item deleted",
        })

def viewleaves(request):
    user = request.user
    today = date.today()
    startdate = today -timedelta(days = today.weekday())
    enddate = startdate + timedelta(days = 365)
    leave = leaves.objects.filter(leavedate__range = [today,enddate]).order_by('leavedate')
    user = request.user
    personalleaves = leaves.objects.filter(user = user)
    userinfo = employeestatus.objects.get(user = user)
    for x in personalleaves:
        if x.leavedate < today and x.status == "APPROVED":
            x.status = "TAKEN"
            x.save()
        if x.leavedate < today and x.status == "PENDING":
            x.delete()
            userinfo.leaves = userinfo.leaves + 1
            userinfo.save()
    
    isboss = False
    if userinfo.role == 'Boss':
        isboss =True
    else:
        isboss =False
    return render(request, "leave.html",
    {"leaves" : leave,
    "isboss": isboss,
    "userinfo": userinfo,
    "personalleaves": personalleaves,}
    )

def getleaves(request):
    # Query for requested data
    user_leave = leaves.objects.filter(status = "APPROVED")
    return JsonResponse([leave.serialize() for leave in user_leave], safe=False)

def approve(request,id):
        leave = leaves.objects.get(pk = id)
        if leave.status == "PENDING":
            leave.status = "APPROVED"
            leave.save()
            user = leave.user
            userinfo = employeestatus.objects.get(user = user)
            userinfo.leaves = userinfo.leaves - 1
            userinfo.save()
        else:
            leave.status = "PENDING"
            leave.save()
            user = leave.user
            userinfo = employeestatus.objects.get(user = user)
            userinfo.leaves = userinfo.leaves + 1
            userinfo.save()
        return JsonResponse({
            "message": "Leave Approved",
        })

def applyleave(request):
    applydate = request.POST["applydate"]
    x = leaves.objects.create(leavedate = applydate, user = request.user)
    x.save()
    y = employeestatus.objects.get(user = request.user)
    y.leaves = y.leaves - 1
    y.save()
    return HttpResponseRedirect(reverse("leave"))
