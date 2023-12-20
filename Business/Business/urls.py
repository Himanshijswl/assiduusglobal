from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter


# Creating Router object
router = DefaultRouter()

#register StudentViewSet with Router
router.register('productapi', views.ProductModelViewSet, basename='product'),
router.register('orderapi', views.OrderModelViewSet, basename='order'),
router.register('line_itemapi', views.Line_ItemModelViewSet, basename='line_item'),


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),

    
]
