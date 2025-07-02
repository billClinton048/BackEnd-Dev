from django.shortcuts import render, redirect
from .forms import RegistrationForm

# My Views 
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    
    else:
        form = RegistrationForm()
    return render(request, 'register.html',{f'form': form})


def success(request):
    return render(request, 'success.html')

