from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import JobApplication, JobList, JobCategory, UserProfile
from .forms import JobApplicationForm, JobListForm, UserProfileForm
from django.contrib.auth.models import User 


def job_list(request):
    job_listings = JobList.objects.all()
    categories = JobCategory.objects.all()

    category_filter = request.GET.get('category')
    location_filter = request.GET.get('location')

    if category_filter:
        job_listings = job_listings.filter(category__name=category_filter)
    if location_filter:
        job_listings = job_listings.filter(location=location_filter)

    context = {
        'job_listings': job_listings,
        'categories': categories,
    }

    return render(request, 'home.html', context)

@login_required
def apply_job(request, job_id):
    job = JobList.objects.get(id=job_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.user = request.user
            application.save()
            messages.success(request, 'Job application submitted successfully.')
            return redirect('profile')
    else:
        form = JobApplicationForm()
    return render(request, 'apply.html', {'form': form, 'job': job})

def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            UserProfile.objects.create(user=user)
            return redirect('job_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('job_list')

@login_required
def profile(request):
    user = request.user
    applied_jobs = JobApplication.objects.filter(user=user)
    context = {
        'user': user,
        'applied_jobs': applied_jobs,
    }
    return render(request, 'profile.html', context)

def job_details(request, job_id):
    job = JobList.objects.get(pk=job_id)
    return render(request, 'details.html', {'job': job})



@login_required
def edit_profile(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
        else:
            messages.error(request, 'There was an error in the form submission. Please check your inputs.')

    else:
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'profile_form': profile_form})

@login_required
def job_listings(request):
    job_listings = JobList.objects.filter(user=request.user)
    return render(request, 'job_listings.html', {'job_listings': job_listings})

@login_required
def create_job(request):
    if request.method == 'POST':
        form = JobListForm(request.POST)
        if form.is_valid():
            job_listing = form.save(commit=False)
            job_listing.user = request.user
            job_listing.save()
            return redirect('job_listings')
    else:
        form = JobListForm()
    return render(request, 'create_job.html', {'form': form})

@login_required
def edit_job(request, job_id):
    job_listing = get_object_or_404(JobList, pk=job_id)
    
    # Check if the logged-in user is the owner of the job listing
    if job_listing.user != request.user:
        return redirect('job_listings')

    if request.method == 'POST':
        form = JobListForm(request.POST, instance=job_listing)
        if form.is_valid():
            form.save()
            return redirect('job_listings')
    else:
        form = JobListForm(instance=job_listing)

    return render(request, 'edit_job.html', {'form': form, 'job_listing': job_listing})

@login_required
def delete_job(request, job_id):
    job_listing = get_object_or_404(JobList, pk=job_id)
    
    # Check if the logged-in user is the owner of the job listing
    if job_listing.user != request.user:
        return redirect('job_listings')

    if request.method == 'POST':
        job_listing.delete()
        return redirect('job_listings')
    return render(request, 'delete_job.html', {'job_listing': job_listing})

@login_required
def job_applications(request, job_id):
    job_listing = get_object_or_404(JobList, id=job_id)
    applications = JobApplication.objects.filter(job=job_listing)
    return render(request, 'job_applications.html', {'job_listing': job_listing, 'applications': applications})

@login_required
def view_user_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = UserProfile.objects.get(user=user)
    return render(request, 'view_user_profile.html', {'user_profile': user_profile})
