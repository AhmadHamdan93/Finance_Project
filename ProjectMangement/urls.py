from django.urls import path
from . import views

urlpatterns =[
    path('',views.show_all_project,name="allProjects"),
    path('typeproject/',views.showTypeProject,name="typeOFProject"),
    path('about/',views.showUS,name="aboutUS"),
    #  paths for operations on data
    path('insertProject/',views.insertProject,name="insertproject"),
    path('deleteProject/',views.deleteProject,name="deleteproject"),
    path('updateProject/',views.updateProject,name="updateproject"),
    # paths for type of project
    path('insertType/',views.insertType,name="inserttype"),
    path('deleteType/',views.deleteType,name="deletetype"),
    path('updateType/',views.updateType,name="updatetype"),

]