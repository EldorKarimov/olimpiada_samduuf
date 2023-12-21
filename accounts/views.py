from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

from .forms import RegisterForm

class LoginOrRegisterView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        register_form = RegisterForm()
        context = {
            'login_form':login_form,
            'register_form':register_form
        }
        return render(request, 'auth.html', context)

    def post(self, request):
        login_form = AuthenticationForm(data = request.POST)
        register_form = RegisterForm(data = request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, "Foydalanuvchi nomi yoki parol noto'g'ri. Iltimos tekshirib qayta urinib ko'ring.")
            return redirect('login')
            

        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Siz muvaffaqqiyatli ro'yhatdan o'tdingiz. Marhamat tizimga kiring")
            return redirect('login')
            
        else:
            messages.error(request, "Bunday foydalanuvchi avval ro'yhatdan o'tgan")
            return redirect('login')
            

def logout_view(request):
    logout(request)
    return redirect('login')