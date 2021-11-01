from django.urls import path
from .import views
import name

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_index, name='projects'),
    # path('contact/', views.contact, name='contact'),
    # path("<int:pk>/", views.project_detail, name="project_detail"),
]
