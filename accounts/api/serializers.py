from rest_framework.reverse import reverse

from accounts.forms import ContactAppUser, UserCreationForm, User
from rest_framework.serializers import ModelSerializer


class ContactAppUserSerializer(ModelSerializer):

    class Meta:
        form_class = ContactAppUser
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'password'
        )

    def get_absolute_url(self):
        return reverse('login')