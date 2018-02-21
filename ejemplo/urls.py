from django import urls
from rest_framework import routers
from users import api as api_user
from django.conf.urls import url, include

router = routers.SimpleRouter()
router.trailing_slash = '/?'
router.register(r'v1/customer', api_user.CustomerViewSet, base_name='user')
router.register(r'v1/office', api_user.OfficeViewSet, base_name='match')

urlpatterns = [
    url(r'^', include(router.urls))
]
