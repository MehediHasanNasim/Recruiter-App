from django.urls import path, include

urlpatterns = [
    path('test/', include('core.rest.urls.user')),
]
