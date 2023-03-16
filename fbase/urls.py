from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import EmployeeView

router=DefaultRouter()
router.register('empview',EmployeeView,basename="Employee lists")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
