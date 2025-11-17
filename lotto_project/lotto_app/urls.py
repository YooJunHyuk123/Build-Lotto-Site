from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('buy/', views.buy_lotto, name='buy_lotto'),
    path('check/', views.check_lotto, name='check_lotto'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
    path('admin/lotto/', views.lotto_draw, name='lotto_draw'),
    path('admin/check/', views.admin_check, name='admin_check'),
]
