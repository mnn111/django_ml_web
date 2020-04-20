from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('mainframe/', views.mainframe, name='mainframe'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='ml_home'), name='logout'),
    path('titanic', views.titanic, name='titanic'),
    path('titanic_pred', views.titanic_pred, name='titanic_pred'),
]
