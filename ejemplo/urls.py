from django import urls
from rest_framework import routers
from users import api as api_user
from orders import api as api_orders
from django.conf.urls import url, include

router = routers.SimpleRouter()
router.trailing_slash = '/?'
router.register(r'v1/customer', api_user.CustomerViewSet, base_name='user')
router.register(r'v1/office', api_user.OfficeViewSet, base_name='office')
router.register(r'v1/products', api_orders.ProductViewSet, base_name='product')
router.register(r'v1/orders', api_orders.OrderViewSet, base_name='order')

urlpatterns = [
    url(r'', include(router.urls))
]
