from django.urls import path,include
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name="main_app/index.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),  
    path('signup/', views.signup, name='signup'),
    path('journals/<int:pk>/', views.journal_detail, name='journal_detail'),
    path('journals/create/', views.journal_create, name='journal_create')
]