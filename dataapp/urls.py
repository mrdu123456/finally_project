from django.urls import path
from dataapp import views
app_name='dataapp'
urlpatterns = [
    path('home/',views.home,name='home'),
    path('menu/',views.menu,name='menu'),
    path('introduce/',views.introduce,name='introduce'),
    path('ajax1/',views.ajax1,name='ajax1'),
    path('ajax2/',views.ajax2,name='ajax2'),
    path('ajax2/',views.ajax2,name='ajax2'),
    path('ajax3/',views.ajax3,name='ajax3'),
    path('ajax4/',views.ajax4,name='ajax4'),
]