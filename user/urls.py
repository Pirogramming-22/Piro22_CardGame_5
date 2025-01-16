from django.urls import path
from user import views

app_name="user"

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),  # 가정된 대시보드 뷰
]