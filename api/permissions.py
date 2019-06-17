from rest_framework import permissions
from  .models import *

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):

        django_user = request.user
        try:
            mUser = User.objects.get(auth_user = django_user)
        except User.DoesNotExist:
            return False

        if request.method == 'GET' and mUser.typeOfUser=='intern':
            # for interns
            return True
        return mUser.typeOfUser == 'admin'