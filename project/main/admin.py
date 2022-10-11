from django.contrib import admin
from .models import *

# Register your models here.

class TestAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'count', 'time', 'passing_score']

admin.site.register(Category, TestAdmin)



class AnswerAdmin(admin.StackedInline):

    model = Answer


admin.site.register(Answer)

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

    
admin.site.register(Product, QuestionAdmin)


