from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest import views

router = DefaultRouter()
router.register(r'people', views.PeopleViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]

