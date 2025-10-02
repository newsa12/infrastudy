from django.db import models

class Order(models.Model):
    class Status(models.TextChoices):
        PENDING_PAYMENT = "pending_payment"
        PAYMENT_FAILED = "payment_failed"
        PENDING_ACCEPT = "pending_acceptance"
        REJECTED = "rejected"
        PREPARING = "preparing"
        READY_FOR_PICK = "ready_for_pickup"
        IN_TRANSIT = "in_transit"
        DELIVERED = "delivered"

    status = models.CharField(
        max_length=32,
        choices=Status.choices,
        default=Status.PENDING_PAYMENT,
    )
    amount = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #생명주기 상태 전이 규칙
    ALLOWED = {
        Status.PENDING_PAYMENT: {Status.PAYMENT_FAILED, Status.PENDING_ACCEPT},
        Status.PENDING_ACCEPT: {Status.REJECTED, Status.PREPARING},
        Status.PREPARING: {Status.READY_FOR_PICK},
        Status.READY_FOR_PICK: {Status.IN_TRANSIT},
        Status.IN_TRANSIT: {Status.DELIVERED},
    }

    def can_transition_to(self,new_status: str) -> bool:
        return new_status in self.ALLOWED.get(self.status, set())
    
    def apply_status(self, new_status: str):
        if not self.can_transition_to(new_status):
            raise ValueError(f"Illegal transition: {self.status} -> {new_status}")
        self.status = new_status
        self.save(update_fields=["status", "updated_at"])