
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from .serializers import ContactAppUserSerializer


class ContactAppUserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ContactAppUserSerializer
