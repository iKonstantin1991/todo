from rest_framework.permissions import BasePermission


class UserDeletePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.is_superuser and not request.user.is_superuser:
            return False
        return bool(request.user and request.user.is_staff)
