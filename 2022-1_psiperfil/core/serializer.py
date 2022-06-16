from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {"password": {"write_only": True, "min_length": 8}}
        fields = (
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "bio",
            "user_permissions",
            "is_active",
            "is_staff",
        )
        read_only_fields = (
            "user_permissions",
            "is_active",
            "is_staff",
        )

    def update(self, instance, validated_data):
        instance.name_permission = validated_data.get(
            "name_permission", instance.name_permission
        )
        instance.email_permission = validated_data.get(
            "email_permission", instance.email_permission
        )
        instance.bio_permission = validated_data.get(
            "bio_permission", instance.bio_permission
        )
        instance.save()

        if instance.name_permission == False:
            User.objects.filter(pk=instance.user.id).update(first_name="", last_name="")
        if instance.email_permission == False:
            User.objects.filter(pk=instance.user.id).update(email="")
        if instance.bio_permission == False:
            User.objects.filter(pk=instance.user.id).update(bio="")
        return instance


class LGPDPermissionsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("get_username")
    email = serializers.SerializerMethodField("get_email")
    first_name = serializers.SerializerMethodField("get_first_name")
    last_name = serializers.SerializerMethodField("get_last_name")
    bio = serializers.SerializerMethodField("get_bio")

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_bio(self, obj):
        return obj.user.bio

    class Meta:
        model = LGPDPermissions
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "bio",
            "name_permission",
            "email_permission",
            "bio_permission",
            "created_at",
            "updated_at",
        )

    def update(self, instance, validated_data):
        instance.name_permission = validated_data.get(
            "name_permission", instance.name_permission
        )
        instance.email_permission = validated_data.get(
            "email_permission", instance.email_permission
        )
        instance.bio_permission = validated_data.get(
            "bio_permission", instance.bio_permission
        )
        instance.save()

        if instance.name_permission == False:
            User.objects.filter(pk=instance.user.id).update(first_name="", last_name="")
        if instance.email_permission == False:
            User.objects.filter(pk=instance.user.id).update(email="")
        if instance.bio_permission == False:
            User.objects.filter(pk=instance.user.id).update(bio="")
        return instance


class FormAttentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormAttention
        fields = "__all__"


class FormPersonalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FormPersonality
        fields = "__all__"


class FormLearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormLearning
        fields = "__all__"
