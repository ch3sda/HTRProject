from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
from django.utils.text import slugify

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    discord = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

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
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    banner_color_start = models.CharField(max_length=20, default='blue')
    banner_color_end = models.CharField(max_length=20, default='indigo')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=100, default='Default Title')
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='course_thumbnails/', blank=True)
    logo = models.ImageField(upload_to='course_logos/', blank=True)
    cover = models.ImageField(upload_to='course_covers/', blank=True)
    banner_color_start = models.CharField(max_length=20, default='blue')
    banner_color_end = models.CharField(max_length=20, default='indigo')
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(default=timezone.now)
    path = models.ForeignKey(Path, on_delete=models.CASCADE, related_name='courses')


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Section(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='section_images/', blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Question(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    answer = models.TextField(blank=True)
    hint = models.TextField(blank=True, null=True)  # Add this line to include hint

    def __str__(self):
        return self.text

class Lab(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='labs', default=None)
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='lab_thumbnails/', blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

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
