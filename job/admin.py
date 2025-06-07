from django.contrib import admin
from job.models import JobPosting, JobApplication
from shared.base_admin import BaseModelAdmin

@admin.register(JobPosting)
class JobPostingAdmin(BaseModelAdmin):
    list_display = (
        'uid',
        'title',
        'recruiter',
        'location',
        'salary',
        'status',
        'created_at'
    )
    list_filter = (
        'status',
        'location',
        'created_at',
    )
    search_fields = (
        'title',
        'description',
        'recruiter__email',
        'recruiter__first_name',
        'recruiter__last_name',
    )
    readonly_fields = (
        'uid',
        'created_at',
        'updated_at',
    )
    fieldsets = (
        ('Basic Information', {
            'fields': (
                'uid',
                'recruiter',
                'title',
                'description'
            )
        }),
        ('Job Details', {
            'fields': (
                'location',
                'salary',
                'deadline'
            )
        }),
        ('Status', {
            'fields': (
                'status',
            )
        }),
        ('Timestamps', {
            'fields': (
                'created_at',
                'updated_at'
            )
        }),
    )
    raw_id_fields = ('recruiter',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_per_page = 20

@admin.register(JobApplication)
class JobApplicationAdmin(BaseModelAdmin):
    list_display = (
        'uid',
        'job',
        'candidate',
        'status',
        'created_at'
    )
    list_filter = (
        'status',
        'job__title',
    )
    search_fields = (
        'job__title',
        'candidate__email',
        'cover_letter',
    )
    readonly_fields = (
        'uid',
        'created_at',
        'updated_at',
    )
    raw_id_fields = ('job', 'candidate')