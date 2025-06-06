from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsRecruiter, IsCandidate

class RecruiterTestView(APIView):
    permission_classes = [IsAuthenticated, IsRecruiter]
    
    def get(self, request):
        return Response({"message": "Welcome Recruiter!"})

class CandidateTestView(APIView):
    permission_classes = [IsAuthenticated, IsCandidate]
    
    def get(self, request):
        return Response({"message": "Welcome Candidate!"})