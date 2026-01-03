from common.viewsets import TenantModelViewSet
from common.permissions import IsManagerOrAdmin, IsTaskOwnerOrAdmin
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(TenantModelViewSet):
    serializer_class = TaskSerializer

    filterset_fields = ['status', 'project']
    search_fields = ['title', 'description']

    def get_queryset(self):
        return Task.objects.filter(
            organization=self.request.user.organization
        )

    def get_permissions(self):
        if self.action in ["create", "destroy"]:
            return [IsManagerOrAdmin()]
        elif self.action in ["update", "partial_update"]:
            return [IsTaskOwnerOrAdmin()]
        return super().get_permissions()
