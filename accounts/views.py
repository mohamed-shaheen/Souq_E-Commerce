from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate
from .models import Profile
from .forms import UserForm, ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user =authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

    else:
        form = UserCreationForm()

    context = {'form' : form}

    return render(request, 'registration/signup.html', context) 

@login_required
def profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    if request.user == profile.user:
        context = {'profile' : profile }
    else:
        raise Http404     
    return render(request, 'profile.html', context)           