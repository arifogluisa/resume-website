from django.contrib import admin
from .models import Profile, Skill, Contact

admin.site.register(Profile)
admin.site.register(Contact)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')
