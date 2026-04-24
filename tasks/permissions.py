from rest_framework.permissions import BasePermission


class IsProjectMember(BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "participants"):
            return request.user in obj.participants.all()

        if hasattr(obj, "project"):
            return request.user in obj.project.participants.all()

        return False


class IsProjectOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "creator"):
            return obj.creator == request.user

        if hasattr(obj, "project"):
            return obj.project.creator == request.user

        return False


class IsTaskAuthorOrAssignee(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user or
            obj.assignee == request.user
        )