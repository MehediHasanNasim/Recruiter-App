from django.db import models
from shared.base_model import BaseModel
from core.models import User

class JobPosting(BaseModel):
    recruiter = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='job_postings'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        null=True,
        blank=True
    )
    deadline = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('DRAFT', 'Draft'),
            ('PUBLISHED', 'Published'),
            ('CLOSED', 'Closed'),
        ],
        default='DRAFT'
    )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Job Posting"
        verbose_name_plural = "Job Postings"
    
    def __str__(self):
        return f"{self.title} - {self.location}"
    

class JobApplication(BaseModel):
    job = models.ForeignKey(
        JobPosting, 
        on_delete=models.CASCADE,
        related_name='applications'
    )
    candidate = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='job_applications'
    )
    cover_letter = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('PENDING', 'Pending'),
            ('REVIEWED', 'Reviewed'),
            ('REJECTED', 'Rejected'),
            ('ACCEPTED', 'Accepted'),
        ],
        default='PENDING'
    )
    
    class Meta:
        unique_together = ['job', 'candidate']
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.candidate.email} -> {self.job.title}"