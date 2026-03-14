from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('employes/', EmployeListView.as_view(), name='employe_list'),
    path('employes/add/', EmployeCreateView.as_view(), name='employe_add'),
    path('employes/<int:pk>/edit/', EmployeUpdateView.as_view(), name='employe_edit'),
    path('employes/<int:pk>/delete/', EmployeDeleteView.as_view(), name='employe_delete'),
]