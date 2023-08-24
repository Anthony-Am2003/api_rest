from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'companys',views.CompanyViews)

urlpatterns = [
    path('', include(router.urls))
]