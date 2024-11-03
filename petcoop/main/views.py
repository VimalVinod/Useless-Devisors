from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import PetProfile  # Import the PetProfile model
from .forms import PetProfileForm  # Import the form for PetProfile

# Home page view
def index(request):
    return render(request, 'index.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

# Signup view
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            try:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Account created successfully!')
                return redirect('login')
            except IntegrityError:
                messages.error(request, 'Username already exists. Please choose another one.')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'signup.html')

# Citizenship exam selection view
@login_required
def citizenship_exam(request):
    # Prevent access if the user has already completed their certificate
    if hasattr(request.user, 'petprofile') and request.user.petprofile.certificate_completed:
        messages.warning(request, "You have already completed your exams and received your certificate.")
        return redirect('welcome')

    if request.method == 'POST':
        pet_name = request.POST.get('pet_name')
        request.session['pet_name'] = pet_name  # Store pet name in session
        tier = request.POST.get('tier')
        return redirect(f'tier_{tier}_exam')  # Redirect to the correct tier exam
    return render(request, 'citizenship_exam.html')

# Tier Exam views
@login_required
def tier_1_exam(request):
    return render(request, 'tier_1_exam.html')

@login_required
def tier_2_exam(request):
    return render(request, 'tier_2_exam.html')

@login_required
def tier_3_exam(request):
    return render(request, 'tier_3_exam.html')

# Submit Tier Exam views
@login_required
def submit_tier_1_exam(request):
    if request.method == 'POST':
        messages.success(request, "You have successfully completed Tier 1 exam!")
        return redirect('tier_2_exam')
    return redirect('tier_1_exam')

@login_required
def submit_tier_2_exam(request):
    if request.method == 'POST':
        messages.success(request, 'You have completed Tier 2 exam!')
        return redirect('tier_3_exam')
    return redirect('tier_2_exam')

@login_required
def submit_tier_3_exam(request):
    if request.method == 'POST':
        messages.success(request, 'You have completed Tier 3 exam!')
        
        # Mark the certificate as completed for the user
        pet_profile = PetProfile.objects.get(user=request.user)
        pet_profile.certificate_completed = True
        pet_profile.save()  # Save the profile instance
        return redirect('welcome')
    return redirect('tier_3_exam')

# Pet Profile Creation View
@login_required
def create_pet_profile(request):
    # Check if the pet profile exists or create a new one
    pet_profile, created = PetProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PetProfileForm(request.POST, request.FILES, instance=pet_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Pet profile updated successfully!")
            return redirect('welcome')
    else:
        form = PetProfileForm(instance=pet_profile)

    return render(request, 'create_pet_profile.html', {'form': form})

# Welcome view
@login_required
def welcome(request):
    pet_name = request.session.get('pet_name', 'Pet')
    
    # Retrieve pet profile and check if certificate is completed
    pet_profile = PetProfile.objects.filter(user=request.user).first()
    certificate_completed = pet_profile.certificate_completed if pet_profile else False

    return render(request, 'welcome.html', {
        'pet_name': pet_name,
        'certificate_completed': certificate_completed,
        'pet_profile': pet_profile,
    })
