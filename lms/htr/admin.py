from django.contrib import admin
from .models import (
    User, UserSettings, Course, Lab, Path, Competition,
    CompetitionParticipation, Rank, Leaderboard, Enrollment,
    Discussion, Transaction, Section, Question,CustomUser, UserProfile
)
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    # Define any custom configurations for UserAdmin here
    pass

admin.site.register(CustomUser, UserAdmin)
admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(UserSettings)
admin.site.register(Lab)
admin.site.register(Competition)
admin.site.register(CompetitionParticipation)
admin.site.register(Rank)
admin.site.register(Leaderboard)
admin.site.register(Enrollment)
admin.site.register(Discussion)
admin.site.register(Transaction)

class CourseInline(admin.StackedInline):  # or admin.TabularInline for a more compact view
    model = Course
    extra = 1  # Number of extra forms to display

class SectionInline(admin.StackedInline):
    model = Section
    extra = 1

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

@admin.register(Path)
class PathAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CourseInline]  # Include the CourseInline here

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'path', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [SectionInline]

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('section', 'text')

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'discord')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_photo', 'facebook', 'twitter', 'linkedin', 'instagram']

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')