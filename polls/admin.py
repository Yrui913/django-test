from django.contrib import admin

# Register your models here.

from .models import Question

# Customize the admin form
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date','question_text']

admin.site.register(Question, QuestionAdmin)