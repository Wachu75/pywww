from django.contrib import admin
from .models import Candidate, Carerr


class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'gender', 'career']
    search_fields = ['name']
    list_per_page = 10

admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Carerr)