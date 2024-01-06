from django.contrib import admin
from .models import QuizModel, Question, Answer, Result, QuizUser

class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ['answer_name', 'is_right']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_name']
    fields = ['question_name', 'quiz']
    list_filter = ['quiz']
    search_fields = ['question_name']
    inlines = [AnswerInlineModel]

@admin.register(QuizModel)
class QuizModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'lang', 'is_publish', 'start_time', 'end_time')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'author')  
    list_filter = ('lang', 'is_publish')  
    list_editable = ('is_publish', )

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'question_count', 'correct_question_count',)
    search_fields = ('user__full_name', 'quiz__name')  # Enable searching by user and associated quiz
    list_filter = ('quiz',)  # Add filter for sorting by quiz

@admin.register(QuizUser)
class QuizUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'start_time', 'end_time', 'expiration_time', 'completed', 'get_time')
    search_fields = ('user__full_name', 'quiz__name')  # Enable searching by user and associated quiz
    list_filter = ('quiz', 'completed')  # Add filters for sorting by quiz and completion status
