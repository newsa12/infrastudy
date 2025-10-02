from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "status", "amount", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

#상태 변경 입력 전용 (단일 PUT 바디용)
class StatusUpdateSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Order.Status.choices)

    def validate(self, attrs):
        order: Order = self.context["order"]
        new_status = attrs["status"]
        if not order.can_transition_to(new_status):
            raise serializers.ValidationError(f"Illegal transition: {order.status} -> {new_status}")
        return attrs