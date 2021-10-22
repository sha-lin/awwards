from rest_framework import serializers
from .models import Profile, Project


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("user", "bio", "profile_photo")

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("title", "project_image", "description", "link", "pub_date", "average_ratings", "no_of_ratings")
