

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from django.contrib.auth.decorators import login_required

@login_required
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer  # Link request to customer
            service_request.save()
            return redirect('request_tracking')  # Redirect after successful submission
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit_request.html', {'form': form})
