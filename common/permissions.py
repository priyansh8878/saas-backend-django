from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "ADMIN"


class IsManagerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role in ["ADMIN", "MANAGER"]
        )


class IsMember(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "MEMBER"

class IsTaskOwnerOrAdmin(BasePermission):
    """
    - Any authenticated user can access the view
    - Only admin or assigned user can modify the task
    """

    def has_permission(self, request, view):
        # Allow access to the view itself
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Admin can do anything
        if request.user.role == "ADMIN":
            return True

        # Assigned member can update
        return obj.assigned_to == request.user