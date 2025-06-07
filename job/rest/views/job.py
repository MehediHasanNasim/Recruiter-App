from rest_framework import generics, permissions
from job.models import JobPosting
from job.rest.serializers.job import JobPostingSerializer
from core.permissions import IsRecruiter

class JobPostingListCreateView(generics.ListCreateAPIView):
    serializer_class = JobPostingSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]
    
    def get_queryset(self):
        return JobPosting.objects.filter(recruiter=self.request.user)

class JobPostingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobPostingSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]
    lookup_field = 'uid'
    
    def get_queryset(self):
        return JobPosting.objects.filter(recruiter=self.request.user)