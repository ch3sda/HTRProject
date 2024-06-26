# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
from django.utils.text import slugify

# Custom User model
class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='htr_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='htr_user_set_permissions', blank=True)

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferences = models.JSONField()
    
class Path(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cover = models.ImageField(upload_to='path_covers/', blank=True)
    thumbnail = models.ImageField(upload_to='path_thumbnails/', blank=True)
    logo = models.ImageField(upload_to='path_logos/', blank=True)
    slug = models.SlugField(unique=True, blank=True)  # Add this line
    created_at = models.DateTimeField(default=timezone.now)
    banner_color_start = models.CharField(max_length=20, default='blue')  # Gradient start color
    banner_color_end = models.CharField(max_length=20, default='indigo')  # Gradient end color
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Course(models.Model):
    title = models.CharField(max_length=100, default='Default Title')
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='course_thumbnails/', blank=True)
    logo = models.ImageField(upload_to='course_logos/', blank=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(default=timezone.now)
    path = models.ForeignKey(Path, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Lab(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='labs')
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='lab_thumbnails/', blank=True)
    created_at = models.DateTimeField(default=timezone.now)

class Competition(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class CompetitionParticipation(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='participations')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participations')
    score = models.IntegerField()
    rank = models.IntegerField()

class Rank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ranks')
    rank_title = models.CharField(max_length=50)
    points = models.IntegerField()

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboards')
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='leaderboards')
    position = models.IntegerField()

class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(default=timezone.now)

class Discussion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discussions')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
