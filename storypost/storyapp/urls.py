from django.urls import path
from . import views

urlpatterns = [

    path('',views.hello,name='hello'),
    path('test-ajax/',views.test_ajax),
    path('test-response/',views.ajax_for_json)
    
]