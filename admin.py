from .models import *
from django import forms
from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.models import User

@admin.register(Consumer)
class ConsumerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "image", "content"]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "message"]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "consumer", "comment", "rating"]
