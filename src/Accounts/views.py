from django.http import HttpResponse
from django.shortcuts import render, redirect
from Accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class CustomSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields


def signup(request):
    context = {}
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-index')
        else:
            context["errors"] = form.errors

    form = CustomSignupForm()
    context["form"] = form

    return render(request, "accounts/signup.html", context=context)


def profile(request):
    return HttpResponse(f"Bienvenue {request.user.username}")
