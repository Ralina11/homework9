import random
from django.conf import settings
from main.services import sendmail
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User



class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    # success_url = reverse_lazy('users:verify_email_sent')

    def form_valid(self, form):
        if form.is_valid:
            fields = form.save()
            sendmail(
                f'Для верификации почты пройдите по ссылке http://127.0.0.1:8000/users/confirm_email/{fields.pk}',
                (fields.email,),
            )
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(11)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Новый пароль:{new_password}. Изменить пароль вы сможете в личном кабинете',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('main:index'))