import random
import string


from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm, UserPasswordResetForm
from users.models import User


def generate_password():
    """Генерация рандомного пароля"""
    characters = string.ascii_letters + string.digits + string.punctuation
    list_of_characters = ('_'.join(characters).split('_'))
    random.shuffle(list_of_characters)
    generated_password = ''.join([character for character in list_of_characters[:random.randint(8, 14)]])
    return generated_password


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            sended_message = f'Аккаунт с почтой {new_form.email} успешно зарегистрирован'
            send_mail('Оповещение о регистрации', sended_message, EMAIL_HOST_USER, [str(new_form.email)])

        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def password_reset(request):
    if request.method == 'POST':
        form = UserPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email__contains=email)
                new_password = generate_password()
                user.set_password(new_password)
                user.save()
                send_mail(
                    'Восстановление пароля',
                    f'Ваш новый пароль: {new_password}',
                    EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                )
            except User.DoesNotExist:
                print(f'пользователь с таким {email} не найден')
    else:
        form = UserPasswordResetForm

    return render(request, 'users/password_reset_form.html', {'form': form})
