from django.urls import path, include

urlpatterns = [
    path('job/', include('job.rest.urls.job')),
    path('applications/', include('job.rest.urls.application')),
]