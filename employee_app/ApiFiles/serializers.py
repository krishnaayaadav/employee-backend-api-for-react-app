
from employee_app.models import Employee
from rest_framework import serializers

# Employees Serializer here
class EmployeeSerializer(serializers.Serializer):
    """Employee serializer to serialize their obj"""
    id    = serializers.IntegerField(required=False)
    name  = serializers.CharField()
    email = serializers.EmailField()
    department = serializers.CharField()
    position   = serializers.CharField()
    job_role   = serializers.CharField()
    salary     = serializers.IntegerField()
    avtar      = serializers.ImageField()
    status     = serializers.CharField(required=False)
    
    # custom serializer validations here
    def validate(self, attrs):
        method = self.context['method']
        email = None
        email = attrs.get('email', None)
        
        # request method  POST
        if method == 'POST':
            if not email: 
                raise serializers.ValidationError('Email field is required')
            
            else:
                try:
                    emp = Employee.objects.get(email=email)
                except:
                    # if exception raise than ok that means no emp exist with this email
                    pass

                else:
                    # other emp exist so raise validation errors
                    raise serializers.ValidationError('Employee already registered with this email address kindly use different email')
        
        # For PUT and PATCH validations
        else:
            if not email:
                pass
            else:
                try:
                    emp = Employee.objects.filter(email = email).exclude(pk = self.context['id'])
                except:
                    pass
                else:
                    if (emp.count() > 0):
                        raise serializers.ValidationError('Employee already registered with  this email address use other email id')

        return attrs # returning validated_data
    
    # create method to allow creation on emp obj
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    
    # update method here
    def update(self, instance, validated_data):
        # instance: represent the old data of employee
        # validated_data: represetns new data coming for updation
        instance.name       = validated_data.get('name',  instance.name)
        instance.email      = validated_data.get('email',  instance.email)
        instance.avtar      = validated_data.get('avtar',  instance.avtar)
        instance.status     = validated_data.get('status', instance.status)
        instance.salary     = validated_data.get('salary', instance.salary)
        instance.department = validated_data.get('department', instance.department)
        instance.position   =  validated_data.get('position',  instance.position)
        instance.job_role   = validated_data.get('job_role',   instance.job_role)
        instance.save()
        return instance
        