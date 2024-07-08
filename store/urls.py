
from django.urls import path,include
from  .import views
urlpatterns = [

    path('a/',views.index,name='index'),


]
