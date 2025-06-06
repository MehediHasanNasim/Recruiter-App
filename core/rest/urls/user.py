from django.urls import path
from core.rest.views.user import CandidateTestView, RecruiterTestView

urlpatterns = [
    path('candidate/', CandidateTestView.as_view(), name='candidate-test'),
    path('recruiter/', RecruiterTestView.as_view(), name='recruiter-test'),
]
