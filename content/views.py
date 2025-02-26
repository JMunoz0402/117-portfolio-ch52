from django.shortcuts import render
from .models import Project
from django.views.generic import ListView
from .forms import ProjectForm

# Create your views here.
def project_list_view(request):
    my_projects = Project.objects.all()

    return render(request, 'content/project_list.html', {"projects": my_projects})

def project_new_view(request):
    form = ProjectForm()
    return render(request, 'content/project_new.html',{'form': form})