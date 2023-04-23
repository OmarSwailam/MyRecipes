from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


class AdminOnlyCanDeletePermission(BasePermission):
    """
    Custom permission to only allow users to list, retrieve, or create tags.
    Admin users can delete tags.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.method == "POST":
            # Allow users to list, retrieve, or create
            return True
        elif (request.user.is_authenticated and request.user.is_staff) and (
            request.method in SAFE_METHODS or request.method == "DELETE"
        ):
            # Allow admin users to delete
            return True
        else:
            return False
