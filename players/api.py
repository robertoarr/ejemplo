from rest_framework import viewsets
# Test test
# Another test
# fix

class PlayerViewSet(viewsets.GenericViewSet):
    permission_classes = []
    authentication_classes = []

    def list(self, request):

        pass

    def retrieve(self, request, pk):
        pass

    def create(self, request):
        pass

    def partial_update(self, request, pk):
        # Aquí wa a trabajar
        
        pass

    def delete(self, request, pk):
        pass
