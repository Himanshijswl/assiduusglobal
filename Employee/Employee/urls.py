from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter


# Creating Router object
router = DefaultRouter()

#register StudentViewSet with Router
router.register('employeeapi', views.EmployeeModelViewSet, basename='employee')


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),

    
]
