from django.contrib.auth import get_user_model
from djoser.conf import settings
from djoser.serializers import UserCreateSerializer

User = get_user_model()


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            "password",
            "is_staff",
        )
        extra_kwargs = {"is_staff": {"required": False}}
