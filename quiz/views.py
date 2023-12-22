from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
import random
from django.http import HttpResponse
from accounts.models import CustomUser
from django.contrib import messages
from django.utils import timezone

from .models import QuizModel, Question, Answer, Result

def get_session(request):
    session_id = request.session.session_key
    if not session_id:
        session_id.session.create()
        session_id = request.session.session_key
    return session_id

class QuizDetailView(LoginRequiredMixin, View):
    def get(self, request, slug):
        quiz = QuizModel.objects.get(slug = slug)
        context = {
            'quiz':quiz
        }
        return render(request, 'quiz_detail.html', context)
    
class QuizPageView(LoginRequiredMixin, View):
    def get(self, request, slug):
        quiz = QuizModel.objects.get(slug = slug)
        user = CustomUser.objects.get(username = request.user.username)
        request.session['start_quiz_time'] = timezone.now().isoformat()
        if not user.session_id:
            user.session_id = get_session(request)
            user.save()
        if get_session(request) != user.session_id:
            messages.error(request, "Siz boshqa qurilmadan kirishga urindingiz")
            return redirect('quiz_detail', quiz.slug)
        
        questions = Question.objects.filter(quiz = quiz)
        questions = random.sample(list(questions), 3)
        answers = Answer.objects.all()
        answers = list(answers)
        random.shuffle(answers)
        context = {
            'questions':questions,
            'answers':answers
        }
        
        return render(request, 'quiz_page.html', context)
        
    def post(self, request, slug):
        correct = 0
        
        quiz = QuizModel.objects.get(slug = slug)
        questions = Question.objects.filter(quiz = quiz)
        questions = random.sample(list(questions), 3)
        answers = Answer.objects.all()
        answers = list(answers)
        random.shuffle(answers)
        
        for question in questions:
            print(request.POST.get(question.question_name))
            if request.POST.get(question.question_name) == 'True':
                correct += 1
            quiz = question.quiz
        
        Result.objects.create(
            question_count = len(questions),
            correct_question_count = correct,
            user = request.user,
            quiz = quiz
        )
        total = correct * 100 / len(questions)
        context = {
            'correct':correct,
            'wrong':len(questions) - correct,
            'number_of_questions':len(questions),
            'total':round(total, 2)
        }
        return render(request, 'result.html', context)  