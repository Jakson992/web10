from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required


class RegisterView(View):
    template_name = 'users/registration.html'
    form_class = RegisterForm

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect(to="quotes:root")
    #     return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            return redirect('quotes:root')  # Перенаправлення на головну сторінку з цитатами після успішної реєстрації

        return render(request, self.template_name, {'form': form})


class CustomLogoutView(View):
    @login_required
    def get(self, request):
        logout(request)
        return redirect('quotes:root')


class LoginView(View):
    template_name = 'users/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('quotes:root')  # Перенаправление на главную страницу после успешного логина
            else:
                form.add_error(None, 'Неверные учетные данные. Пожалуйста, попробуйте еще раз.')

        return render(request, self.template_name, {'form': form})
    #
    # def get_success_url(self):
    #     # Возвращает URL-шаблон, на который нужно перенаправить пользователя после успешного логина
    #     return reverse(
    #         'quotes:root')  # Здесь 'quotes:root' - это имя URL-шаблона, на который нужно перенаправить пользователя
