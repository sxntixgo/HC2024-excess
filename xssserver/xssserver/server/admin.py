from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import GameUser, TargetServer, Attempt

class GameUserInline(admin.StackedInline):
    model = GameUser
    can_delete = False
    verbose_name_plural = 'gameusers'

class UserAdmin(BaseUserAdmin):
    inlines = (GameUserInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(TargetServer)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(GameUser)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Attempt)
class AuthorAdmin(admin.ModelAdmin):
    pass