from rest_framework_mongoengine import serializers
from Employee.models import Employees
class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeID','first_name','Dept_name')
