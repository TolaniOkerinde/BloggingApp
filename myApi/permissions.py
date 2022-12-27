from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view ,obj):
        """Check user is trying to edit their own profile """

        #safe methods methods that dont make changeseg get 

        if request.method in permissions.SAFE_METHODS:
            return True
            #if its get user can still view others profile 

        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to edit their own status"""

    def has_object_permission(self, request, view ,obj):
        """Check user is trying to edit their own status """

        #safe methods methods that dont make changeseg get 

        if request.method in permissions.SAFE_METHODS:
            return True
            #if its get user can still view others profile 

        return obj.userProfile.id == request.user.id

