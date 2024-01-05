from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
import random
from django.http import HttpResponse
from accounts.models import CustomUser
from django.contrib import messages
from django.utils import timezone

from .models import QuizModel, Question, Answer, Result, QuizUser

def get_session(request):
    session_id = request.session.session_key
    if not session_id:
        session_id.session.create()
        session_id = request.session.session_key
    return session_id

class QuizDetailView(LoginRequiredMixin, View):
    def get(self, request, slug):
        quiz = QuizModel.objects.get(slug = slug)
        result = Result.objects.filter(user = request.user).exists()

        context = {
            'quiz':quiz,
            'result':result
        }
        return render(request, 'quiz_detail.html', context)
    
class QuizPageView(LoginRequiredMixin, View):
    def get(self, request, slug):
        quiz = QuizModel.objects.get(slug = slug)
        user = CustomUser.objects.get(username = request.user.username)
        quiz_user, created = QuizUser.objects.get_or_create(user=request.user, quiz=quiz)
        quiz_user.start_time = timezone.now()
        quiz_user.expiration_time = quiz_user.start_time + timezone.timedelta(minutes=30)
        quiz_user.save()

        if not user.session_id:
            user.session_id = get_session(request)
            user.save()
        if get_session(request) != user.session_id:
            messages.error(request, "Siz boshqa qurilmadan kirishga urindingiz")
            return redirect('quiz_detail', quiz.slug)
        
        questions = Question.objects.filter(quiz = quiz)
        if len(questions) >= 30:
            questions = random.sample(list(questions), 30)
        else:
            questions = random.sample(list(questions), len(questions))
        answers = Answer.objects.all()
        answers = list(answers)
        random.shuffle(answers)
        context = {
            'questions':questions,
            'answers':answers,
            'quiz_user':quiz_user,
            'x':30
        }
        
        response = render(request, 'quiz_page.html', context)
        response.set_cookie('quiz_start_time', timezone.now().isoformat(), max_age=60 * 1)
        return response
        
    def post(self, request, slug):
        result = Result.objects.filter(user = request.user).exists()
        if result:
            return HttpResponse("Xatolik! Siz avval test topshirgansiz.")
        
        correct = 0
        
        quiz = QuizModel.objects.get(slug = slug)
        quiz_user = QuizUser.objects.get(user = request.user, quiz = quiz)
        questions = Question.objects.filter(quiz = quiz)
        if len(questions) >= 30:
            questions = random.sample(list(questions), 30)
        else:
            questions = random.sample(list(questions), len(questions))
        answers = Answer.objects.all()
        answers = list(answers)
        random.shuffle(answers)
        
        
        for question in questions:
            print(request.POST.get(f"{question.id}-hack"))
            if request.POST.get(f"{question.id}-hack"):
                correct += 1
            quiz = question.quiz
        
        Result.objects.create(
            question_count = len(questions),
            correct_question_count = correct,
            user = request.user,
            quiz = quiz
        )
        quiz_user.end_time = timezone.now()
        total = correct * 100 / len(questions)
        context = {
            'correct':correct,
            'wrong':len(questions) - correct,
            'number_of_questions':len(questions),
            'total':round(total, 2)
        }
        quiz_user.completed = True
        quiz_user.save()
        return render(request, 'result.html', context)  