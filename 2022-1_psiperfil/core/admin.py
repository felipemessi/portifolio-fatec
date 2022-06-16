from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import Permission

from .forms import UserChangeForm, UserCreationForm
from .models import (FormAttention, FormLearning, FormPersonality,
                     LGPDPermissions, User)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos Personalizados", {"fields": ("bio",)}),
    )
    list_display_links = (
        "username",
        "bio",
    )
    search_fields = auth_admin.UserAdmin.search_fields + ("bio",)
    list_display = auth_admin.UserAdmin.list_display + ("bio",)
    list_per_page = 20


@admin.register(LGPDPermissions)
class LGPDPermissionsAdmin(admin.ModelAdmin):
    list_display_links = (
        "user",
        "name_permission",
        "email_permission",
        "bio_permission",
    )
    search_fields = (
        "user",
        "name_permission",
        "email_permission",
        "bio_permission",
        "created_at",
        "updated_at",
    )
    list_display = (
        "user",
        "name_permission",
        "email_permission",
        "bio_permission",
        "created_at",
        "updated_at",
    )
    list_per_page = 20


@admin.register(FormAttention)
class FormAttentionAdmin(admin.ModelAdmin):
    list_display_links = ("user",)
    search_fields = ("user",)
    list_display = ("user", "questao1", "questao2", "questao3", "questao4", "questao5")
    list_per_page = 20


@admin.register(FormPersonality)
class FormPersonalityAdmin(admin.ModelAdmin):
    list_display = ("user", "questao1", "questao2", "questao3")
    list_per_page = 20


@admin.register(FormLearning)
class FormLearningAdmin(admin.ModelAdmin):
    list_display = ("user", "questao1", "questao2", "questao3", "questao4", "questao5")
    list_per_page = 20
