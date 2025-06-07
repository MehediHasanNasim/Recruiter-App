from django.urls import path
from job.rest.views.job import (
    JobPostingListCreateView,
    JobPostingRetrieveUpdateDestroyView
)

urlpatterns = [
    path('', JobPostingListCreateView.as_view(), name='job-list-create'),
    path('<uuid:uid>/', JobPostingRetrieveUpdateDestroyView.as_view(), name='job-detail'),
]