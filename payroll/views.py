from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee, Attendance, IncomeTax

def payroll_dashboard(request):
    employees = Employee.objects.all()
    months = Attendance.objects.values_list('month', flat=True).distinct()
    return render(request, "payroll/dashboard.html", {'employees': employees, 'months': months})

def get_payroll_data(request, emp_no, month):
    try:
        employee = Employee.objects.get(emp_no=emp_no)
        attendance = Attendance.objects.get(emp_no=emp_no, month=month)
        income_tax = IncomeTax.objects.get(emp_no=emp_no)
        
        gross_pay = (employee.basic_pay / 30) * attendance.days_present
        net_pay = gross_pay * (1 - income_tax.tax_percentage / 100)
        
        # Convert to integer
        gross_pay = int(gross_pay)
        net_pay = int(net_pay)

        return JsonResponse({'gross_pay': gross_pay, 'net_pay': net_pay})
    except (Employee.DoesNotExist, Attendance.DoesNotExist, IncomeTax.DoesNotExist) as e:
        return JsonResponse({'error': str(e)}, status=400)
