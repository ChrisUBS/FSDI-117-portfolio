from django.urls import path
from portfolio import views

urlpatterns = [
    path("projects/", views.ProjectsListPageView, name="projects_list"),
    path("experience-and-education/", views.ExperienceAndEducationPageView, name="experience_and_education"),
]