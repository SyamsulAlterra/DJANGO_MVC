from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.welcome_page, name='welcome page'),
    path('sign_in/', views.sign_in, name='sign in'),
    path('sign_up/', views.sign_up, name='sign up'),
    path('success/', views.success_sign_up, name='success sign up'),
    path('hompage/', views.homepage, name='homepage'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)