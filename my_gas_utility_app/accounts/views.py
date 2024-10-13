from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm
from django.contrib.auth import login
def home(request):
    return render(request, 'home.html')
def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')  # Redirect to a home page or dashboard
        
    else:
        form = CustomerRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
