from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .form import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnienie zakończyło sukcesem.')
                else:
                    return HttpResponse('Konto zablokowane')
            else:
                return HttpResponse('Nieprawidłowe dane uwierzytelniające.')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


# Create your views here.
