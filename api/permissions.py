from rest_framework.permissions import BasePermission


class AdminOrAuthorCanOnlyEditOrDelete(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in ('PUT', 'DELETE'):
            return bool(
                obj.author == request.user
                or request.user.is_staff
            )
        else:
            return bool(request.user.is_authenticated)
