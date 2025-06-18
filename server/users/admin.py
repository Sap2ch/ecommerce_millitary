from django.contrib import admin
from .models import Profile, FFLVerify

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'slug', 'avatar')
    # prepopulated_fields = {'slug': ('user',)}

class FFLAdmin(admin.ModelAdmin):
    list_display = ('pk', 'image', 'user', 'date_create')
    list_display_links = ('user',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(FFLVerify, FFLAdmin)