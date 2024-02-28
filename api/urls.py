from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'test', views.test, basename='test')


urlpatterns = [
    path('test/', views.test.as_view()),
    path("create-pdf", views.CreatePDF.as_view()),
    

]
