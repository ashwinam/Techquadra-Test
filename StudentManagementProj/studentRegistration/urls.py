from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('create/', views.StudentRegistrationView.as_view(), name='student-create'),
    path("login/", views.UserLoginView.as_view(), name='login'),
    path("logout/", views.logoutUser, name='logout-user'),
    path('a-panel/', TemplateView.as_view(template_name='admin_panel.html'), name='admin-panel'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard-view'),
    path('reports/', views.ReportView.as_view(), name='report-view'),
]