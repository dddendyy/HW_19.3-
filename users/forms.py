from django.contrib.auth.forms import UserCreationForm, UserChangeForm, forms

from users.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
        template_name = 'users/register.html'


class UserProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar')


class UserPasswordResetForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=50)
