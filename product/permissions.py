from .models import User
from rest_framework.permissions import BasePermission, SAFE_METHODS


class SellerPer(BasePermission):
    def has_permission(self, request, view):
        seller = User.objects.filter(is_seller=True, phone=request.user.phone).exists()
        return seller


class IsUserOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user
