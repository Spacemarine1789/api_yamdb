from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Permissions for change or delete Admin only"""
    message = 'Данное действие разрешено только администратору!'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == 'admin'


class IsStaffOrAuthorOrReadOnly(permissions.BasePermission):
    """Permissions for change or delete Admin only"""
    message = 'Данное действие разрешено только администратору!'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role != 'admin' and request.user.role != 'moderator':
            return obj.author == request.user
        else:
            return True
