from rest_framework.serializers import ModelSerializer
from managers.models import Manager, StaffManager, ActiveManager


class ManagerSerializer(ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'


class StaffManagerSerializer(ModelSerializer):
    class Meta:
        model = StaffManager
        fields = '__all__'

