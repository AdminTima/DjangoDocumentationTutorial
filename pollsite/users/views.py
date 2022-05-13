from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse


def register(request):
    err = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1']
        repeat_pass = request.POST['pass2']
        if username and password and repeat_pass:
            if password == repeat_pass:
                try:
                    user = User.objects.create_user(username, password=password)
                    return HttpResponseRedirect(reverse('polls:index'))
                except Exception:
                    err = 'Error occured'
    return render(request, 'users/reg.html')
