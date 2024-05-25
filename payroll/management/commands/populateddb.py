from django.core.management.base import BaseCommand
from payroll.models import Employee, Attendance, IncomeTax

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        employees = [
            (1, 10000),
            (2, 15000),
            (3, 20000)
        ]
        
        attendances = [
            (1, 'April', 25),
            (1, 'May', 23),
            (1, 'June', 21),
            (2, 'April', 25),
            (2, 'May', 23),
            (2, 'June', 21),
            (3, 'April', 25),
            (3, 'May', 23),
            (3, 'June', 21)
        ]
        
        taxes = [
            (1, 15),
            (2, 20),
            (3, 25)
        ]
        
        for emp_no, basic_pay in employees:
            Employee.objects.create(emp_no=emp_no, basic_pay=basic_pay)
        
        for emp_no, month, days_present in attendances:
            Attendance.objects.create(emp_no_id=emp_no, month=month, days_present=days_present)
        
        for emp_no, tax_percentage in taxes:
            IncomeTax.objects.create(emp_no_id=emp_no, tax_percentage=tax_percentage)
        
        self.stdout.write(self.style.SUCCESS('Database populated successfully'))
