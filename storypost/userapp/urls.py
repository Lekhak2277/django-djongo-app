from django.urls import path
from . import views
from .views import user_form

urlpatterns = [
    path('', views.user_form, name="user_form"),
]
