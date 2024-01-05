from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class QuizModel(BaseModel):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length = 120)
    lang = models.CharField(max_length = 15)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(upload_to='media/images')
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_publish = models.BooleanField(default = False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Quizzes"

class Question(BaseModel):
    question_name = models.TextField()
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_name
    
class Answer(BaseModel):
    answer_name = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_name
    
class Result(BaseModel):
    question_count = models.PositiveIntegerField()
    correct_question_count = models.PositiveIntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)  # null=True ni qo'shing
    quiz = models.ForeignKey(QuizModel, on_delete=models.SET_NULL, null=True)  # null=True ni qo'shing

    def __str__(self):
        return self.user.full_name if self.user else "Anonymous User"


class QuizUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default = timezone.now())
    end_time = models.DateTimeField(null=True, blank=True)
    expiration_time = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.name}"