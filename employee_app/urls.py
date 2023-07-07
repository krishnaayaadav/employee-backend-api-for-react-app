from django.urls import path,include
from employee_app import views

urlpatterns = [
    # path('home/', views.home),

    path('api/', include('employee_app.ApiFiles.api_urls'))
]
