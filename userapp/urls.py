from django.urls import path
from userapp import views
app_name='userapp'

urlpatterns=[
    path('login/',views.login,name='login'),
    path('loginlogic/',views.loginlogic,name='loginlogic'),
    path('regist/',views.regist,name='regist'),
    path('registlogic/',views.registlogic,name='registlogic'),
    path('dong/',views.dong,name='dong'),
    path('ajax1/',views.ajax1,name='ajax1'),
    path('ajax2/',views.ajax2,name='ajax2'),
    path('ajax4/',views.ajax4,name='ajax4'),
    path('ajax5/',views.ajax5,name='ajax5'),
]