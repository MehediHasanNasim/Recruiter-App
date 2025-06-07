from rest_framework import serializers
from job.models import JobApplication, JobPosting
from datetime import datetime

class JobApplicationSerializer(serializers.ModelSerializer):
    candidate = serializers.HiddenField(default=serializers.CurrentUserDefault())
    job = serializers.SlugRelatedField(
        queryset=JobPosting.objects.all(),
        slug_field='uid' 
    )
    class Meta:
        model = JobApplication
        fields = [
            'uid',
            'job',
            'candidate',
            'cover_letter',
            'status',
            'created_at'
        ]
        read_only_fields = ['uid', 'status', 'created_at']
    
    def validate(self, data):
        job = data['job']
        candidate = data['candidate']
        
        # Check if candidate is applying
        if candidate.role != 'CANDIDATE':
            raise serializers.ValidationError("Only candidates can apply for jobs")
        
        # Check deadline
        if job.deadline and job.deadline < datetime.now().astimezone():
            raise serializers.ValidationError("Application deadline has passed")
            
        # Check existing application
        if JobApplication.objects.filter(job=job, candidate=candidate).exists():
            raise serializers.ValidationError("You have already applied to this job")
            
        return data