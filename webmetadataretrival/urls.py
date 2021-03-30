
from django.contrib import admin
from django.urls import path
from frontend import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('documentation/', views.documentation, name='documentation'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
