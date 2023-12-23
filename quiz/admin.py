from django.contrib import admin
from .models import QuizModel, Question, Answer, Result, QuizUser

@admin.register(QuizModel)
class QuizModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug":['name']}

class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ['answer_name', 'is_right']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_name']
    fields = ['question_name', 'quiz']
    inlines = [AnswerInlineModel]



@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['question_count', 'correct_question_count', 'user', 'quiz', 'created']

admin.site.register(QuizUser)