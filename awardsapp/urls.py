from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import ListProfileView, ListProjectView

urlpatterns=[
    path('',views.index, name = 'index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.update, name='update'),
    path('upload_project/', views.upload_project, name='upload_project'),
    path('project/<project_id>/',views.project,name ='project'),
    path('rate/<project_id>/',views.rate,name ='rate'),
    path('search/', views.search_results, name='search_results'),
    path('api/profile/', ListProfileView.as_view(), name="profile-all"),
    path('api/project/', ListProjectView.as_view(), name="project-all")
]