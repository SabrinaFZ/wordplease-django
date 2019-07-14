from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        # Endpoint de listado (GET): solo admin
        # Edpoint de creacion (POST): cualquier usuario
        # Endpoint de detalle (GET): usuario autenticado sólo a sus datos o admin a todos
        # Endpoint de actualizacion (PUT): usuario autenticado sólo a sus datos o admin a todos
        # Endpoint de borrado (DELETE): usuario autenticado sólo a sus datos o admin a todos
        if view.action == 'create' or request.user.is_superuser:
            return True

        return request.user.is_authenticated and view.action in ['retrieve', 'update', 'destroy']

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj