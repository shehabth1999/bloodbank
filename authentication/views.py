from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomAuthenticationForm, CustomUserCreationForm

def auth_view(request):
    login_form = CustomAuthenticationForm()
    register_form = CustomUserCreationForm()

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'Login':
            email = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            print("user", user)

            if user is not None:
                login(request, user)
                return redirect('home')  # Replace with your desired redirect URL
            else:
                return render(request, 'authentication/auth.html', {'login_form': login_form, 'register_form': register_form, 'login_error': True, 'login_error_msg': 'Invalid email or password'})

        elif action == 'Signup':
            register_form = CustomUserCreationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save(commit=False)
                user.email = user.email.lower()  # Ensure email is lowercase
                user.save()
                login(request, user)  # Automatically login the user after registration
                return redirect('home')  # Replace with your desired redirect URL
            else:
                # Print form errors for debugging
                print(register_form.errors)
                return render(request, 'authentication/auth.html', {'login_form': login_form, 'register_form': register_form, 'register_error': True})

    return render(request, 'authentication/auth.html', {'login_form': login_form, 'register_form': register_form})


def logout_view(request):
    logout(request)
    return redirect('auth')