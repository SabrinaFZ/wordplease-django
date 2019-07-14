from rest_framework.permissions import BasePermission

class PostPermission(BasePermission):

    def has_permission(self, request, view):
        if view.action == 'retrieve':
            return True

        return request.user.is_authenticated or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (obj.owner == request.user or request.user.is_superuser)