from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Team, Plan

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
        )

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = (
            "id",
            "name",
            "max_leads",
            "max_clients",
            "price"
        )

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)
    plan = PlanSerializer(read_only=True)

    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "members",
            "created_by",
            "plan",
            "plan_end_date"
        )