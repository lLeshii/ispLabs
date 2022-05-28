from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.contrib.auth import logout
from homepage.forms import  RegisterUserForm, LoginUserForm
from django.http import HttpResponseRedirect
import logging
logger = logging.getLogger("main_logger")
logger.setLevel(logging.DEBUG)
# Create your views here.


class HomePageView(TemplateView):
    template_name = "homepage/homepage.html"
    logger.info("use HomePageView")


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "us_log/register.html"
    logger.info("use RegisterUserView")

    def form_valid(self, form):
        user = form.save()
        user.save()
        return HttpResponseRedirect(settings.LOGIN_URL)


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = "us_log/login.html"
    success_url = reverse_lazy("homepage")
    logger.info("use LoginUserView")


class LogoutUserView(LoginRequiredMixin, View):
    logger.info("use LogoutUserView")
    def get(self, request):
        logout(request)

        return HttpResponseRedirect(settings.LOGIN_URL)