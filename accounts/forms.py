from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'password1',
            'password2'
        )