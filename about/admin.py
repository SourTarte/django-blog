from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About) #This decorator is used for registering classes, unlike how we registered the models below
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
