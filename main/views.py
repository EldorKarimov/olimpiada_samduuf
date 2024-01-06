from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse

from quiz.models import QuizModel, Result, QuizUser
from accounts.models import CustomUser

class HomePageView(View):
    def get(self, request):
        form = ContactForm()
        quizzes = QuizModel.objects.filter(is_publish = True)
        user_count = CustomUser.objects.all().count()
        result_count = Result.objects.all().count()
        context = {
            'quizzes':quizzes,
            'form':form,
            'user_count':user_count,
            'result_count':result_count
        }
        return render(request, 'home.html', context)
    def post(self, request):
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Murojaat muvaffaqqiyatli yuborildi")
            return redirect('home')
        
class ResultListView(View):
    def get(self, request):
        quiz_user = QuizUser.objects.get(user = request.user)
        x = quiz_user.end_time - quiz_user.start_time
        print(type(x))
        return HttpResponse(type(x))