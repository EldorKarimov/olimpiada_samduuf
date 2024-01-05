from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm
from django.contrib import messages

from quiz.models import QuizModel

class HomePageView(View):
    def get(self, request):
        form = ContactForm()
        quizzes = QuizModel.objects.filter(is_publish = True)
        context = {
            'quizzes':quizzes,
            'form':form
        }
        return render(request, 'home.html', context)
    def post(self, request):
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Murojaat muvaffaqqiyatli yuborildi")
            return redirect('home')