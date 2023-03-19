from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

# views.py


class CustomLoginView(LoginView):
    template_name = 'User/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')
