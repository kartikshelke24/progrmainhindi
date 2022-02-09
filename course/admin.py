from django.contrib import admin

from course.models import Course, CourseComment
from course.models import Playlist

# Register your models here.
admin.site.register(Course)
admin.site.register(CourseComment)

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/tinyMCEinject.js',)