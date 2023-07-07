
from employee_app.models import Employee
from .serializers import EmployeeSerializer

# rest_framework imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

#  response status code
ok_res      = status.HTTP_200_OK
created     = status.HTTP_201_CREATED
not_found   = status.HTTP_404_NOT_FOUND
no_content  = status.HTTP_204_NO_CONTENT
bad_request = status.HTTP_400_BAD_REQUEST
not_allowed = status.HTTP_405_METHOD_NOT_ALLOWED

# base class for applying throttle permision and authentication schemes instead applying one by one better to created base class and use it
class AnonUserAPI(APIView):
    throttle_classes = []   # throttle schemes her
    permission_classes = [] # permissions 
    authentication_classes = []  # authentication classes here

# api for get and post data of employees
class EmployeeAPI(AnonUserAPI):
    """This class will provide functionality of fetch all emp data and post new emp into our db via post request.
       No parameters are required
       Method allowed: [GET, POST]
    """
    
    # get request to fetch all emp data from db
    def get(self, request, format=None):
        all_emp = Employee.objects.all()
        serializer = EmployeeSerializer(all_emp, many=True)
        return Response(serializer.data,status=ok_res)
    
    # post request here to add/insert new emp data into db
    def post(self, request, format=None):

        serializer = EmployeeSerializer(data=request.data, context={'method': request.method})
        if serializer.is_valid():
            serializer.save()
            name = str(serializer.validated_data['name']).title()
            res  = {
                'msg': f'Congrats! Employee as {name} created successfully! ',
                'data': serializer.data
            }
            return Response(res, status=created)
        else:
            return Response(serializer.errors, status=bad_request)

# this class provide functionality of update, delete and details page of employee etc.
class EmployeesAPI(AnonUserAPI):
    """This class provide functionality of detail page, update, deletion etc
       Parameter as empId is required
       Method Allowed: [GET, PUT, PATCH, DELETE]
    """

    # get single employee detail page
    def get(self, request, empId, format=None):

        if not empId:  #user has not provided any 
            return Response({'errors': 'Employee Id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        else:

            try: # 
                emp = Employee.objects.get(pk=empId)

            except Employee.DoesNotExist:
                response = {'errors': '404! Employee not found with id'}
                res_status  = status.HTTP_404_NOT_FOUND
            
            except Employee.MultipleObjectsReturned:
                response = {'errors': '404! Employee not found with id'}
                res_status  = status.HTTP_404_NOT_FOUND
            
            else:
                # we are serializing the emp obj
                serializer = EmployeeSerializer(emp)
                response   = {
                    'data': serializer.data
                }
                res_status  = status.HTTP_200_OK

            finally:

                return Response(response, status=res_status)
    
    # patch for partial updation
    def patch(self, request, empId, format=None):

        if not empId:
            return Response({'errors': 'Employee id is required'}, status=not_found)
        
        else:
            try:
                emp = Employee.objects.get(pk = empId)
            
            except Employee.DoesNotExist:
                return Response({'errors': 'Employee not found with this id'}, status=not_found)
            
            except Employee.MultipleObjectsReturned:
                return Response({'errors': 'Employee not found with this id'}, status=not_found)
            
            else:

                serializer = EmployeeSerializer(instance=emp, data=request.data, partial=True, context={'id': emp.id, 'method': request.method})
                if serializer.is_valid():
                    serializer.save()
                    name = serializer.data['name']

                    res = {
                        'msg': f'Congrats! Employee as {str(name).title()} updated successfully',
                        'data': serializer.data
                    }

                    return Response(res, status=ok_res)
                else:
                    return Response(serializer.errors, status=bad_request)

    # put for complete updation
    def put(self, request, empId, format=None):

        if not empId:
            return Response({'errors': 'Employee id is required'}, status=not_found)
        
        else:
            try:
                emp = Employee.objects.get(pk = empId)
            
            except Employee.DoesNotExist:
                return Response({'errors': 'Employee not found with this id'}, status=not_found)
            
            except Employee.MultipleObjectsReturned:
                return Response({'errors': 'Employee not found with this id'}, status=not_found)
            
            else:

                serializer = EmployeeSerializer(instance=emp, data=request.data, context={'id': emp.id, 'method': request.method})
                if serializer.is_valid():
                    serializer.save()
                    name = serializer.data['name']

                    res = {
                        'msg': f'Congrats! Employee as {str(name).title()} updated successfully',
                        'data': serializer.data
                    }

                    return Response(res, status=ok_res)
                else:
                    return Response(serializer.errors, status=bad_request)
                
    # delete for emp obj deletion
    def delete(self, request, empId, format=None):

        if not empId:
            return Response({'errors': 'Employee id is required'}, status=not_found)
        
        else:
            try:
                emp = Employee.objects.get(pk = empId)
            
            except Employee.DoesNotExist:
                return Response({'errors': 'Employee not found with this id'}, status=not_found)
            
            except Employee.MultipleObjectsReturned:
                return Response({'errors': 'Employee not found with this id'}, status=not_found)
            
            else:
                name = emp.name
                emp.delete() # deletion of emp obj here
                res = {
                    'msg': f'Congrats! Employee as {str(name).title()} deleted successfully',
                }

                return Response(res, status=no_content)
                