from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.view),
    path('register', views.register),
    path('regtolog', views.regtolog),
    path('login', views.login),
    path('logtoreg', views.logtoreg),
    path('accountdetails', views.accountdetails),
    path('logout', views.logout),
    path('deposit', views.deposit),
    path('addmoney', views.addmoney),
    path('takemoney', views.takemoney),
    path('withdraw', views.withdraw),
    path('deptoacc', views.deptoacc),
    path('wittoacc', views.wittoacc)


]