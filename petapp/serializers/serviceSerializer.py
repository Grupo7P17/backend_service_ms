from petapp.models.service import Service
from rest_framework        import serializers


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Service
        fields = ['id', 'service', 'cost', 'days', 'category']

    def to_representation(self, obj):
        service    = Service.objects.get(id=obj.id)
        return {
            'id':       service.id,
            'service':  service.service,
            'cost':     service.cost,
            'days':     service.days,
            'category': service.category,
        }