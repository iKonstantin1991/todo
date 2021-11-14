from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.validators import ValidationError

from .models import Task, default_status
from .serializers import TaskSerializer
from .permissions import AdminOrAuthorCanOnlyEditOrDelete


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AdminOrAuthorCanOnlyEditOrDelete]

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = Task.objects.all()
        else:
            queryset = Task.objects.filter(Q(author=self.request.user) |
                                           Q(responsible=self.request.user))
        return queryset

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            serializer.save(
                author=self.request.user,
                status=default_status
            )
        else:
            serializer.save(author=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        if (request.user == task.responsible and
                not (request.user == task.author
                     or request.user.is_staff)):
            status = request.data.get('status', False)
            if status is False:
                raise ValidationError(
                    {'errors': 'You are only allowed to change status'}
                )
            request._full_data = {'status': status}
        return self.update(request, *args, **kwargs)
