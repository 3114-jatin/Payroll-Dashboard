from django.contrib import admin
from django.urls import path
from payroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.payroll_dashboard, name='payroll_dashboard'),
    path('api/payroll/<str:emp_no>/<str:month>/', views.get_payroll_data, name='get_payroll_data'),
]
