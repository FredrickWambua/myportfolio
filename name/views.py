from django.shortcuts import render
from name.models import Project

# Create your views here.
def home(request):
    return render(request, 'index.html')


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)
