from django.conf                          import settings
from rest_framework                       import generics,status
from petapp.models.service                import Service
from rest_framework.response              import Response
from petapp.serializers.serviceSerializer import ServiceSerializer

class ServiceDetailView(generics.RetrieveAPIView):
    queryset           = Service.objects.all()
    serializer_class   = ServiceSerializer

    def get(self, request, *args, **kwargs): 
        return super().get(request, *args, **kwargs)

class ServiceListView(generics.ListAPIView):
    queryset           = Service.objects.all()
    serializer_class   = ServiceSerializer
    def get_queryset(self):
        queryset  = Service.objects.all()
        return queryset


class ServiceUpdateView(generics.UpdateAPIView):
    queryset           = Service.objects.all()
    serializer_class   = ServiceSerializer

    def update(self, request, *args, **kwargs): 
        return super().update(request, *args, **kwargs)

class ServiceDelateView(generics.DestroyAPIView):
    queryset           = Service.objects.all()
    serializer_class   = ServiceSerializer

    def delete(self, request, *args, **kwargs): 
        return super().destroy(request, *args, **kwargs)

class ServiceCreateView(generics.CreateAPIView):
    queryset           = Service.objects.all()
    serializer_class   = ServiceSerializer

    def post(self, request, *args, **kwargs):
        serializer = ServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("se creo un nuevo servicio",status=status.HTTP_201_CREATED)