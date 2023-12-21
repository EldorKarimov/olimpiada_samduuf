from django.db import models
from accounts.models import CustomUser


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
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Quizzes"

class Question(BaseModel):
    question_name = models.CharField(max_length=255)
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
