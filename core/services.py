from .models import Job, Application

def get_active_jobs():
    """Service to fetch only jobs that are currently active."""
    return Job.objects.filter(is_active=True).order_by('-posted_at')