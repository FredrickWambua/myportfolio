from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_index, name='projects'),
    # path("<int:pk>/", views.project_detail, name="project_detail"),
]
