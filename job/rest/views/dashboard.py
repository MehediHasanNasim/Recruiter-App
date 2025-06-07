from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from core.permissions import IsRecruiter
from job.models import JobPosting, JobApplication

class RecruiterDashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]
    
    def get(self, request):
        recruiter = request.user
        
        # Get all job postings for this recruiter
        jobs = JobPosting.objects.filter(recruiter=recruiter)
        
        # Get all applications for this recruiter's jobs
        applications = JobApplication.objects.filter(job__recruiter=recruiter)
        
        # Calculate metrics
        stats = {
            'total_published_jobs': jobs.filter(status='PUBLISHED').count(),
            'total_closed_jobs': jobs.filter(status='CLOSED').count(),
            'total_applications': applications.count(),
            'total_hired': applications.filter(status='ACCEPTED').count(),
            'total_rejected': applications.filter(status='REJECTED').count(),
        }
        
        return Response(stats, status=status.HTTP_200_OK)