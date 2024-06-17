from django.shortcuts import render
from rest_framework import viewsets
from .models import User, UserSettings, Course, Lesson, Lab, Path, PathCourse, Competition, CompetitionParticipation, Rank, Leaderboard, Enrollment, Discussion, Transaction
from .serializers import (
    UserSerializer, UserSettingsSerializer, CourseSerializer, LessonSerializer, LabSerializer, 
    PathSerializer, PathCourseSerializer, CompetitionSerializer, CompetitionParticipationSerializer, 
    RankSerializer, LeaderboardSerializer, EnrollmentSerializer, DiscussionSerializer, TransactionSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserSettingsViewSet(viewsets.ModelViewSet):
    queryset = UserSettings.objects.all()
    serializer_class = UserSettingsSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LabViewSet(viewsets.ModelViewSet):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer

class PathViewSet(viewsets.ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

class PathCourseViewSet(viewsets.ModelViewSet):
    queryset = PathCourse.objects.all()
    serializer_class = PathCourseSerializer

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


def index(request):
    return render(request, 'htr/index.html')

def login(request):
    return render(request, 'htr/login.html')

def signup(request):
    return render(request, 'htr/signup.html')

def dashboard(request):
    return render(request, 'htr/dashboard.html')

def learn(request):
    return render(request, 'htr/learn.html')

def compete(request):
    return render(request, 'htr/compete.html')

def practice(request):
    return render(request, 'htr/practice.html')

def subscribe(request):
    return render(request, 'htr/subscribe.html')

def rank(request):
    return render(request, 'htr/rank.html')

def ISO_27001(request):
    return render(request, 'htr/ISO_27001.html')

def explore(request):
    return render(request, 'htr/explore.html')
