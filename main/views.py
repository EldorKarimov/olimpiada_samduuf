from django.shortcuts import render, redirect
from django.views import View

from quiz.models import QuizModel

class HomePageView(View):
    def get(self, request):
        quizzes = QuizModel.objects.all()
        context = {
            'quizzes':quizzes
        }
        return render(request, 'home.html', context)