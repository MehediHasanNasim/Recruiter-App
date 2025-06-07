from django.urls import reverse
from rest_framework.test import APITestCase
from core.models import User
from jobs.models import JobPosting

class JobPostingAPITestCase(APITestCase):
    def setUp(self):
        self.recruiter = User.objects.create_user(
            email='recruiter@test.com',
            password='testpass123',
            first_name='Recruiter',
            last_name='User',
            role='RECRUITER'
        )
        self.candidate = User.objects.create_user(
            email='candidate@test.com',
            password='testpass123',
            first_name='Candidate',
            last_name='User',
            role='CANDIDATE'
        )
        self.job = JobPosting.objects.create(
            recruiter=self.recruiter,
            title='Test Job',
            description='Test Description',
            location='Remote',
            salary=50000.00,
            status='PUBLISHED'
        )

    def test_recruiter_can_create_job(self):
        self.client.force_authenticate(user=self.recruiter)
        response = self.client.post(reverse('job-list-create'), {
            'title': 'New Job',
            'description': 'New Description',
            'location': 'Office',
            'salary': 60000.00,
            'status': 'DRAFT'
        })
        self.assertEqual(response.status_code, 201)

    def test_candidate_cannot_create_job(self):
        self.client.force_authenticate(user=self.candidate)
        response = self.client.post(reverse('job-list-create'), {
            'title': 'New Job',
            'description': 'New Description',
            'location': 'Office',
            'salary': 60000.00,
            'status': 'DRAFT'
        })
        self.assertEqual(response.status_code, 403)