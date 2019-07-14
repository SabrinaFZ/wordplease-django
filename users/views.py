from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout


# Create your views here.
from django.views import View

from users.forms import LoginForm, SignUpForm

class LoginView(View):

    def render_template_with_form(self, request, form):
        context = {'form': form}
        return render(request, 'users/login.html', context)


    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = LoginForm()
        return self.render_template_with_form(request, form)


    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)

            if user is None:
                messages.error(request, 'Usuario/Contraseña incorrectos')
            else:
                django_login(request, user)
                url = request.GET.get('next', 'home')  # si next esta se devuelve su valor sino se devuelve home
                return redirect(url)

        return self.render_template_with_form(request, form)


class LogoutView(View):

    def get(self, request):
        django_logout(request)
        return redirect('login')


class SignUpView(View):

    def render_template_with_form(self, request, form):
        context = {'form': form}
        return render(request, 'users/sign-up.html', context)


    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = SignUpForm()
        return self.render_template_with_form(request, form)


    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is None:
                messages.error(request, 'Usuario/Contraseña incorrectos')
            else:
                django_login(request, user)

                return redirect('home')

        return self.render_template_with_form(request, form)


