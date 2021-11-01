from django.shortcuts import render
from name.models import Project
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'index.html')


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

# def contact(request):
#     if request.method == 'GET':
#         name = request.GET.get('name')
#         email = request.GET.get('email')
#         message = request.GET.get('message')
#         send_mail(name, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
#         return render(request, 'contact.html', {'email': email})
#     return render(request, 'contact.html')