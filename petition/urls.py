from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.com_list),
    path('<int:id>',views.dom_list),
]