from django.db import models

# 1. Core User Table (Handles both employers and applicants via role flags)
class User(models.Model):
    ROLE_CHOICES = [
        ('EMPLOYER', 'Employer'),
        ('APPLICANT', 'Applicant'),
    ]
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='APPLICANT')
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

# 2. Job Table (Linked directly to User as the employer)
class Job(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs')
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    posted_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# 3. Application Table (Bridge linking User and Job)
class Application(models.Model):
    STATUS_CHOICES = [
        ('APPLIED', 'Applied'),
        ('SCREENING', 'Screening'),
        ('INTERVIEW', 'Interview'),
        ('OFFER', 'Offer'),
        ('REJECTED', 'Rejected'),
    ]
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='APPLIED')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevents a user from submitting duplicate applications to the same job
        unique_together = ('job', 'applicant')

    def __str__(self):
        return f"{self.applicant.username} -> {self.job.title}"