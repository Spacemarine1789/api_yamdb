from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Permissions for change or delete Admin only"""
    message = 'Данное действие разрешено только администратору!'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.role == 'admin'
        )
