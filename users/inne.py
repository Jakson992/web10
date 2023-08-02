from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login , logout
from .forms import RegisterForm, LoginForm


class RegisterView(View):
    template_name = 'users/registration.html'
    form_class = RegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="quotes:root")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quotes:root')  # Перенаправление на главную страницу после успешной регистрации

        return render(request, self.template_name, {'form': form})


class CustomLogoutView(View):
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
                return redirect(
                    'quotes:root')  # Перенаправлення на головну сторінку з цитатами після успішного логування

        return render(request, self.template_name, {'form': form})


<!-- login.html -->

{% extends "quotes/base.html" %}

{% block content %}

<div class="container">
    <h2 class="mb-3">Login User</h2>

    {% if messages %}
    <div class="messages">
        {% for message in messages %}
        <span {% if message.tags %} class="alert alert-{{ message.tags }}" {% endif %}>{{ message }} </span>
        {% endfor %}
    </div>
    {% endif %}

    {% if form.errors and form.non_field_errors %}
    <span class="alert alert-danger" role="alert">{{form.non_field_errors}}</span>
    {% endif %}

    <form method="post">
        {% csrf_token %}
        <div class="mb-3">
            <label class="form-label">Username
                {{ form.username }}
            </label>
            <span>{{form.errors.username}}</span>
        </div>

        <div class="mb-3">
            <label class="form-label">Password
                {{ form.password }}
            </label>
            <span>{{form.errors.password}}</span>
        </div>

        <div class="mb-3">
            <button type="submit" class="btn btn-primary">Send</button>
            <button type="reset" class="btn btn-secondary">Reset</button>
        </div>
    </form>

</div>

{% endblock %}

{% block script %}
{% if user.is_authenticated %}
    <!-- Перенаправлення на бажану сторінку, якщо користувач залогований -->
    <meta http-equiv="refresh" content="0; url={% url 'quotes:root' %}">
{% endif %}
{% endblock %}
