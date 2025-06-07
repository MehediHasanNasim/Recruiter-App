from django.urls import path
from job.rest.views.dashboard import RecruiterDashboardView


urlpatterns = [
    path('', RecruiterDashboardView.as_view(), name='recruiter-dashboard'),
]