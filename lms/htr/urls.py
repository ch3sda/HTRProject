from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, UserSettingsViewSet, CourseViewSet, SectionViewSet, LabViewSet,
    PathViewSet, CompetitionViewSet, CompetitionParticipationViewSet,
    RankViewSet, LeaderboardViewSet, EnrollmentViewSet, DiscussionViewSet, TransactionViewSet,
    course_detail, path_detail, learn
)
from .views import signup_view, login_view, profile_settings
from django.contrib.auth.views import LogoutView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-settings', UserSettingsViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'sections', SectionViewSet)
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
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile-settings/', profile_settings, name='profile_settings'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('learn/', views.learn, name='learn'),
    path('compete/', views.compete, name='compete'),
    path('practice/', views.practice, name='practice'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('rank/', views.rank, name='rank'),
    path('course/<slug>/', views.course_detail, name='course_detail'),
    path('explore/', views.explore, name='explore'),
    path('profile-setting/', views.profile_setting, name='profile_setting'),
    path('learn/path/<slug:slug>/', path_detail, name='path_detail'),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
