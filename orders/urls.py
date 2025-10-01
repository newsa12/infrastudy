from django.urls import path
from .views import OrderListCreate, OrderDetail

urlpatterns = [
    path("api/v1/orders", OrderListCreate.as_view(), name="order-list-create"),
    path("api/v1/orders/<int:order_id>", OrderDetail.as_view(), name="order-detail"),
]