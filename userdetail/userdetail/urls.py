"""userdetail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from enroll import views
from rest_framework.routers import DefaultRouter
from enroll import viewset
from rest_framework_simplejwt.views import TokenVerifyView,TokenRefreshView,TokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration' , views.sign_up,name= 'reg'),
    path('login/',views.user_login,name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.user_logout,name = 'logout'),
    path('', views.add_show,name = 'addandshow'),
    path('delete/<int:id>/', views.delete_data,name = 'deletedata'),
    path('<int:id>/', views.update_data, name='updatedata'),
    path('gettoken/',TokenObtainPairView.as_view(),name = 'gettoken'),
    path('refreshtoken/',TokenRefreshView.as_view(),name = 'refreshtoken'),
    path('verifytoken/',TokenVerifyView.as_view(),name = 'verifytoken')

]
