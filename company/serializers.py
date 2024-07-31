from rest_framework import serializers
from .models import *


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ("address", "phone_number", "email", "lat", "lot")


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ("telegram", "facebook", "instagram", "linkedin")


class ContactWithUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactWithUs
        fields = ("name", "phone_number", "message")

    def create(self, validated_data):
        return ContactWithUs.objects.create(**validated_data)


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ("question", "answer")


class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = ("text",)


class AppInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppInfo
        fields = ("title", "desc")
