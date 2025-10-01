from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as http
from .models import Order
from .serializers import OrderSerializer, StatusUpdateSerializer

class OrderDetail(APIView):
    def get(self, request, order_id):
        o = Order.objects.get(pk=order_id)
        return Response(OrderSerializer(o).data)
    
    def put(self, request, order_id):
        with transaction.atomic():

            o = Order.objects.select_for_update().get(pk=order_id)
            ser = StatusUpdateSerializer(data=request.data, context={"order": o})
            ser.is_valid(raise_exception=True)
            try:
                o.apply_status(ser.validated_data["status"])
            except ValueError as e:
                return Response({"detail": str(e)}, status=http.HTTP_400_BAD_REQUEST)
        return Response(OrderSerializer(o).data, status=http.HTTP_200_OK)
        
#생성/목록 간단 추가 — 테스트용        
class OrderListCreate(APIView):
    def get(self, request):
        qs = Order.objects.all().order_by("-id")[:50]
        return Response({"orders": OrderSerializer(qs, many=True).data})
    
    def post(self, request):
        amount = int(request.data.get("amount", 0))
        o = Order.objects.create(amount=amount)
        return Response(OrderSerializer(o).data, status=http.HTTP_201_CREATED)