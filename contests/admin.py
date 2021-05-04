from django.contrib import admin
from . models import Contest, Exercise, ExerciseComment
# Register your models here.
admin.site.register(Contest)
admin.site.register(Exercise)
admin.site.register(ExerciseComment)

class JobCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'date_posted')