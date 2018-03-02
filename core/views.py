from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from core.forms import SignUpForm
from projects.models import Project
from django.contrib import admin



@login_required
def index(request):
    projects_list = Project.objects.order_by('-project_date')[:5]
    template = loader.get_template('home.html')
    context = {
        'projects_list': projects_list,
    }
    return HttpResponse(template.render(context, request))
#    return render(request, 'home.html')

    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
