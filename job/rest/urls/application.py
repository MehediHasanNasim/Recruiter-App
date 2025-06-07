from django.urls import path
from job.rest.views.application import (
    JobApplicationListCreateView,
    JobApplicationRetrieveView
)

urlpatterns = [
    path('', JobApplicationListCreateView.as_view(), name='application-list-create'),
    path('<uuid:uid>/', JobApplicationRetrieveView.as_view(), name='application-detail'),
]