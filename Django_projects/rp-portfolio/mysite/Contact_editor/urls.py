from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Contacts', views.ContactViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('process_json_object/', views.process_json_object),
]