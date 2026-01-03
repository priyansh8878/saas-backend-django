from common.viewsets import TenantModelViewSet
from common.permissions import IsManagerOrAdmin
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(TenantModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsManagerOrAdmin]

    def get_queryset(self):
        return Project.objects.filter(
            organization=self.request.user.organization
        )
