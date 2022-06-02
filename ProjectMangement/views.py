from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from .models import Project,TypeProject

# Create your views here.

# for render list of projects page
def show_all_project(request):
    pro = Project.objects.all()
    TYPES = TypeProject.objects.all()
    return render(request,'ProjectMangement/listOfProjects.html',{'pro':pro,'TYPES':TYPES})

# for render about page
def showUS(request):
    return render(request,'ProjectMangement/about.html')

# for render list of type page
def showTypeProject(request):
    TYPES = TypeProject.objects.all()
    types = serializers.serialize('json',TypeProject.objects.all())
    return render(request,'ProjectMangement/typeProjects.html',{'types':types,'TYPES':TYPES})

# ------------------------------------
# ------------------------------------
# ------------------------------------
# -------- Main Functions ------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
#  functions for main operations on project table
#  project insert function
def insertProject(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        typeID = request.POST.get('typeID')
        type = TypeProject.objects.get(type=typeID)
        project = Project()
        project.name = name
        project.location = location
        project.dateStart = startDate
        project.dateEnd = endDate
        project.typeProject = type
        project.save()

        return HttpResponse()

# project update function
def updateProject(request):
    if request.method == 'POST':
        pk = request.POST.get('projectID')
        name = request.POST.get('name')
        location = request.POST.get('location')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        typeID = request.POST.get('typeID')
        type = TypeProject.objects.get(type=typeID)
        project = Project.objects.get(id=pk)
        project.name = name
        project.location = location
        project.dateStart = startDate
        project.dateEnd = endDate
        project.typeProject = type
        project.save()
        return HttpResponse()

# project delete function
def deleteProject(request):
    if request.method == 'POST':
        pk = request.POST.get('projectID')
        project = Project.objects.get(id=pk)
        project.delete()
        return HttpResponse()

# ------------------------------------
# ------------------------------------
#  functions for main operations on project table
# insert type function
def insertType(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        typeProject = TypeProject()
        typeProject.type = type
        typeProject.save()
        return HttpResponse()

# update type function
def updateType(request):
    if request.method == 'POST':
        pk = request.POST.get('typeID')
        type = request.POST.get('type')
        typeProject = TypeProject.objects.get(id=pk)
        typeProject.type = type
        typeProject.save()
        return HttpResponse()

# delete type function
def deleteType(request):
        if request.method == 'POST':
            pk = request.POST.get('typeID')
            typeProject = TypeProject.objects.get(id=pk)
            typeProject.delete()
            return HttpResponse()