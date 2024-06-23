# admin.py

from django.contrib import admin
from .models import (
    User, UserSettings, Course, Lesson, Lab, Path, Competition,
    CompetitionParticipation, Rank, Leaderboard, Enrollment,
    Discussion, Transaction
)

admin.site.register(User)
admin.site.register(UserSettings)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Lab)
admin.site.register(Path)
admin.site.register(Competition)
admin.site.register(CompetitionParticipation)
admin.site.register(Rank)
admin.site.register(Leaderboard)
admin.site.register(Enrollment)
admin.site.register(Discussion)
admin.site.register(Transaction)

class PathAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  # This auto-generates the slug from the title
class CourseInline(admin.TabularInline):  # or admin.StackedInline for a more detailed view
    model = Course
    extra = 1  # Number of extra forms to display
class PathAdmin(admin.ModelAdmin):
    inlines = [CourseInline]
    