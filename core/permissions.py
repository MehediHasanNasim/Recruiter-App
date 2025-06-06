from rest_framework.permissions import BasePermission
from core.choices import RoleChoices

class IsRecruiter(BasePermission):
    """Allows access only to recruiter users."""
    def has_permission(self, request, view):
        return request.user.role == RoleChoices.RECRUITER

class IsCandidate(BasePermission):
    """Allows access only to candidate users."""
    def has_permission(self, request, view):
        return request.user.role == RoleChoices.CANDIDATE