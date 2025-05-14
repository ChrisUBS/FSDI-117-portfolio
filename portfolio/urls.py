from django.urls import path
from portfolio import views
from portfolio.views import NewProjectPageView

urlpatterns = [
    path("projects/", views.ProjectsListPageView, name="projects_list"),
    path('projects/new/', views.NewProjectPageView, name='new_project'),
    path("experience-and-education/", views.ExperienceAndEducationPageView, name="experience_and_education"),
]