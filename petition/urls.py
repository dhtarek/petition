from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.com_list),
    path('all',views.dom_list),
    path('<int:id>',views.commune_detail),
    
]