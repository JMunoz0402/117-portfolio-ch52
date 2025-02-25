from django.db import models


# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Technology name: {self.name}"
    

class Project(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to="static/img/")
    repository = models.URLField()
    skill = models.ManyToManyField(Skill)

    def __str__(self):
        return f"{self.name} - ({self.year})"