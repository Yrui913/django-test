from django.contrib import admin

# Register your models here.

from .models import Question, Choice

# Customize the Choice Inline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Customize the admin form
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date','question_text']
    # NOTE:
    # The first element of each tuple in fieldsets is the title of the fieldSet.
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')
    # right filter choices
    list_filter = ['pub_date']
    # search box
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)