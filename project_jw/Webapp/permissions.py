from rest_framework import permissions

class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow staff members to create books.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is authenticated and is_staff
        #return request.user.is_authenticated and request.user.is_staff
         # Check if the user is authenticated and is staff or superuser
        return request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser)
    


    def has_object_permission(self, request, view, obj):
        # Allow staff or superuser to edit or delete any book instance
        # return request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser)
        return request.user.is_authenticated and request.user.is_superuser

    