
from django.db import models

# Create your models here.

class TypeProject(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

class Project(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    dateStart = models.DateField()
    dateEnd = models.DateField()
    typeProject = models.ForeignKey(TypeProject,on_delete=models.CASCADE,null=True,default=1)

    def __str__(self):
        return self.name
