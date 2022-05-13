from django.contrib import admin
from .models import Question, Choice


class ChoiceINLine(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceINLine]
    list_display = ('question_text', 'was_published_recently')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
