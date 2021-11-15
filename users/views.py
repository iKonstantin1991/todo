from djoser import utils
from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.response import Response


class CustomUserViewSet(UserViewSet):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance == request.user:
            utils.logout_user(self.request)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
