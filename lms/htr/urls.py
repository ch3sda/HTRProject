from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, UserSettingsViewSet, CourseViewSet, LessonViewSet, LabViewSet,
    PathViewSet, CompetitionViewSet, CompetitionParticipationViewSet,
    RankViewSet, LeaderboardViewSet, EnrollmentViewSet, DiscussionViewSet, TransactionViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-settings', UserSettingsViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'labs', LabViewSet)
router.register(r'paths', PathViewSet)
router.register(r'competitions', CompetitionViewSet)
router.register(r'competition-participations', CompetitionParticipationViewSet)
router.register(r'ranks', RankViewSet)
router.register(r'leaderboards', LeaderboardViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'discussions', DiscussionViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('learn/', views.learn, name='learn'),
    path('compete/', views.compete, name='compete'),
    path('practice/', views.practice, name='practice'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('rank/', views.rank, name='rank'),
    path('ISO_27001/', views.ISO_27001, name='ISO_27001'),
    path('explore/', views.explore, name='explore'),
]
