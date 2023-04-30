from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()


class UserForm(UserCreationForm):
    """Form for creating a new user"""

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'email', 'password1', 'password2',
        )


# class UserUpdateForm(UserChangeForm):
#     """Form for editing user"""
#     password = None
#
#     class Meta:
#         model = User
#         fields = (
#             'first_name', 'last_name', 'username', 'email', 'password',
#         )
