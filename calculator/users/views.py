from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomSignupForm


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = CustomSignupForm()
    else:
        # Process completed form.
        form = CustomSignupForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)