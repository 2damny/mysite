from django.contrib import admin

# poll app을 관리자 페이지에 보여줄 수 있도록 하는 기능
from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #구분할 수 있는 목록 정의 list_display
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    
    inlines = [ChoiceInline]
    #pub_date필드 별로 목록을 필터링 할 수 있는 필터 사이드 바(list_filter)
    list_filter = ['pub_date']
    #변경목록 맨 위에 검색상자 추가(search_fileds)
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

