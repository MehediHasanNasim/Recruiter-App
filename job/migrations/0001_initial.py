# Generated by Django 5.2.1 on 2025-06-06 22:48

import dirtyfields.dirtyfields
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Unique identifier for this model instance.', unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp indicating when the instance was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Timestamp indicating when the instance was last updated.')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('deadline', models.DateTimeField()),
                ('status', models.CharField(choices=[('DRAFT', 'Draft'), ('PUBLISHED', 'Published'), ('CLOSED', 'Closed')], default='DRAFT', max_length=20)),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_postings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Job Posting',
                'verbose_name_plural': 'Job Postings',
                'ordering': ['-created_at'],
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
