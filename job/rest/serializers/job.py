from rest_framework import serializers
from job.models import JobPosting

class JobPostingSerializer(serializers.ModelSerializer):
    recruiter = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = JobPosting
        fields = [
            'uid',
            'recruiter',
            'title',
            'description',
            'location',
            'salary',
            'deadline',
            'status',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['uid', 'created_at', 'updated_at']
    
    def validate_recruiter(self, value):
        if value.role != 'RECRUITER':
            raise serializers.ValidationError("Only recruiters can create job postings")
        return value