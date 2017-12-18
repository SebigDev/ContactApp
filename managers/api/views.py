from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView, RetrieveDestroyAPIView)
from rest_framework.permissions import (
AllowAny,
IsAuthenticated,
IsAdminUser,
IsAuthenticatedOrReadOnly
)

from managers.api.serializers import ManagerSerializer, StaffManagerSerializer
from managers.models import Manager, StaffManager, ActiveManager


class ManagerListAPIView(ListAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class ManagerCreateAPIView(CreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [AllowAny]


class ManagerRetrieveAPIView(RetrieveAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class ManagerUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class ManagerDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class StaffManagerListAPIView(ListAPIView):
    queryset = StaffManager.objects.all()
    serializer_class = StaffManagerSerializer


class StaffManagerCreateAPIView(CreateAPIView):
    queryset = StaffManager.objects.all()
    serializer_class = StaffManagerSerializer


class StaffManagerRetrieveAPIView(RetrieveAPIView):
    queryset = StaffManager.objects.all()
    serializer_class = StaffManagerSerializer


class StaffManagerUpdateAPIView(RetrieveUpdateAPIView):
    queryset = StaffManager.objects.all()
    serializer_class = StaffManagerSerializer


class StaffManagerDeleteAPIView(RetrieveDestroyAPIView):
    queryset = StaffManager.objects.all()
    serializer_class = StaffManagerSerializer



