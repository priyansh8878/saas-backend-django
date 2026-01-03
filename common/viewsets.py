from rest_framework.viewsets import ModelViewSet

class TenantModelViewSet(ModelViewSet):
    """
    Base ViewSet to enforce tenant isolation
    """

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(organization=self.request.user.organization)

    def perform_create(self, serializer):
        serializer.save(organization=self.request.user.organization)
