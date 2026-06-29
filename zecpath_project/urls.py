from django.contrib import admin
from django.urls import path
from core.views import home, JobAPIView, UserTestAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/jobs/', JobAPIView.as_view(), name='job-api'),       # GET and POST
    path('api/users/', UserTestAPIView.as_view(), name='user-api'), # GET
]