from rest_framework import generics, permissions
from job.models import JobApplication
from job.rest.serializers.application import JobApplicationSerializer
from core.permissions import IsCandidate

class JobApplicationListCreateView(generics.ListCreateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsCandidate]
    
    def get_queryset(self):
        return JobApplication.objects.filter(candidate=self.request.user)

class JobApplicationRetrieveView(generics.RetrieveAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsCandidate]
    lookup_field = 'uid'
    
    def get_queryset(self):
        return JobApplication.objects.filter(candidate=self.request.user)