
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employee_app.urls')),
    path('api/documentation/', include_docs_urls(title='Employee Management API'))

     # media files settings here
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
