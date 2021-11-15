import datetime as dt

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import Task, default_status, statuses


class TaskSerializer(ModelSerializer):
    status = serializers.ChoiceField(
        choices=statuses,
        required=False,
        default=default_status
    )

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'created', 'do_until',
                  'status', 'responsible')

    def validate_do_until(self, value):
        today = dt.date.today()

        if value <= today:
            raise ValidationError(
                {'errors': 'do_until field must be in the future'}
            )

        return value
