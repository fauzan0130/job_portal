from django.db import models
from django.contrib.auth.models import User

class JobCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class JobList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobList, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')
    latest_qualification = models.CharField(max_length=100)
    applied_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    shortlisted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    linkedin_profile = models.URLField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

