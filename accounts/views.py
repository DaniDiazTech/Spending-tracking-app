from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy

from .forms import SignUpForm

class SignUpView(CreateView):
    """
    Allow the User to Create a New Account
    """
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('budget:home')

    # If the form is valid it'll directly login the user and redirect him to the blog.
    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return to_return

