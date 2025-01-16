
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("home", views.home, name="home"),
    path("employees", views.employees, name="employees"),
    path("remove/<int:id>", views.remove_user, name="remove"),
    path("projects", views.project, name="projects"),
    path("getprojects", views.getprojects, name="getprojects"),
    path("addproject", views.addproject, name="addproject"),
    path("markasdone/<int:id>", views.markasdone, name="markasdone"),
    path("addtodo/<str:todovalue>", views.addtodo, name="addtodo"),
    path("removetodo/<int:id>", views.removetodo, name="removetodo"),
    path("leave", views.viewleaves, name="leave"),
    path("getleaves",views.getleaves, name = "getleaves"),
    path("approve/<int:id>", views.approve, name="approve"),
    path("applyleave",views.applyleave, name = "applyleave"),
    path('profile/', views.profile, name='profile'),

]
