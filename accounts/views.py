from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from .forms import SignUpForm, AccountForm
from django.contrib.auth.models import User

from chat.models import Account


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        acc = Account(name=user.username, user=user)
        acc.save()
        return redirect('/accounts/login')


@login_required
def personal_cabinet(request):
    if request.method == "POST":
        acc = Account.objects.get(user=request.user)
        acc_form = AccountForm(request.POST, instance=acc, files=request.FILES)
        if acc_form.is_valid():
            acc_form.save()
            msg = "Changes accepted."
        else:
            msg = "Error. Changes weren't accepted."
    else:
        acc = Account.objects.get(user=request.user)
        acc_form = AccountForm(instance=acc)
        msg = None

    return render(request, 'pers_cab.html', {"form": acc_form, "msg": msg, "acc": acc})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/accounts/login')
