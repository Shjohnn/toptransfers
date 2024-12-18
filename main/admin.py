from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *

admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(Country)
class Country(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'president', 'coach', 'found_date', 'country')
    search_fields = ('name', 'country')
    date_hierarchy = 'found_date'
    list_filter = ('country', 'name')


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'price', 'position', 'number', 'club')
    search_fields = ('name', 'club', 'number', 'position')


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('player', 'old_club', 'new_club', 'price', 'season', 'date')
    search_fields = ('player', 'old_club', 'new_club', 'price')

