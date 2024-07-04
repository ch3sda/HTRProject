# views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from .models import (
    User, UserSettings, Course, Lab, Path, Competition,
    CompetitionParticipation, Rank, Leaderboard, Enrollment,
    Discussion, Transaction, Section, Question , UserProfile ,CustomUser
)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .serializers import (
    UserSerializer, UserSettingsSerializer, CourseSerializer,
    LabSerializer, PathSerializer, CompetitionSerializer,
    CompetitionParticipationSerializer, RankSerializer, LeaderboardSerializer,
    EnrollmentSerializer, DiscussionSerializer, TransactionSerializer,
    SectionSerializer, QuestionSerializer , CustomUserSerializer
)
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserLoginForm, CustomUserChangeForm, UserProfileForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login as django_login  # Rename to avoid conflict with view name
User = get_user_model()
from django.contrib.auth import logout  # Import logout function

@login_required
def profile_settings(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile_setting')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)
    return render(request, 'profile_setting.html', {'user_form': user_form, 'profile_form': profile_form})


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserSettingsViewSet(viewsets.ModelViewSet):
    queryset = UserSettings.objects.all()
    serializer_class = UserSettingsSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class LabViewSet(viewsets.ModelViewSet):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer

class PathViewSet(viewsets.ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

class CompetitionParticipationViewSet(viewsets.ModelViewSet):
    queryset = CompetitionParticipation.objects.all()
    serializer_class = CompetitionParticipationSerializer

class RankViewSet(viewsets.ModelViewSet):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class DiscussionViewSet(viewsets.ModelViewSet):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer    


def some_view(request):
    if 'example_param' not in request.GET:
        raise Http404("This page does not exist")
# Your other views (e.g., index, login, signup, etc.) remain as defined in your previous messages
def index(request):
    return render(request, 'htr/index.html')
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'htr/signup.html', {'form': form})


# Update login_view in views.py
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'htr/login.html', {'form': form, 'error_message': 'Invalid email or password.'})
    else:
        form = UserLoginForm()
    return render(request, 'htr/login.html', {'form': form})




def logout_view(request):
    logout(request)
    return redirect('index')

def dashboard(request):
    recent_paths = Path.objects.order_by('-created_at')[:5]
    context = {
        'recent_paths': recent_paths,
    }
    return render(request, 'htr/dashboard.html' ,context)

def learn(request):
    paths = Path.objects.all()
    return render(request, 'htr/learn.html',{'paths': paths})

def path_detail(request, slug):
    path = get_object_or_404(Path, slug=slug)
    courses = Course.objects.all()
    return render(request, 'htr/path_detail.html', {'path': path,'courses': courses})

def compete(request):
    return render(request, 'htr/compete.html')

def practice(request):
    return render(request, 'htr/practice.html')

def subscribe(request):
    return render(request, 'htr/subscribe.html')

def rank(request):
    return render(request, 'htr/rank.html')

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    sections = course.sections.all()
    context = {
        'course': course,
        'sections': sections,
    }
    return render(request, 'htr/course_detail.html', context)

def explore(request):
    return render(request, 'htr/explore.html')

def profile_setting(request):
    return render(request, 'htr/profile_setting.html')
