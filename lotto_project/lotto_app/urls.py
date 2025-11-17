from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # 사용자 기능
    path('buy/', views.buy_lotto, name='buy_lotto'),
    path('check/', views.check_lotto, name='check_lotto'),

    # 관리자 기능 (admin/ prefix 제거)
    path('lotto/', views.lotto_draw, name='lotto_draw'),
    path('admin_check/', views.admin_check, name='admin_check'),
]
