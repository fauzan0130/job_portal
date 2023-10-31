from django.contrib import admin
from .models import JobList, JobCategory, JobApplication, UserProfile

@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(JobList)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'posted_date', 'user')
    list_filter = ('category', 'location', 'posted_date')
    search_fields = ('title', 'category__name', 'location', 'user__username')

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'user', 'name', 'phone', 'location', 'resume', 'latest_qualification', 'applied_date', 'approved', 'shortlisted')
    list_filter = ('approved', 'shortlisted', 'applied_date')
    search_fields = ('job__title', 'user__username', 'name', 'phone', 'location')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'linkedin_profile', 'website')
