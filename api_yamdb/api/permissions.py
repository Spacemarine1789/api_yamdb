from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Permissions for change or delete Admin only"""
    message = 'Данное действие разрешено только администратору!'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            print(request.user.username)
            print(request.user.role)
            return True
        return request.user.role == 'admin'
