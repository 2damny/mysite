from django.contrib import admin

# poll app을 관리자 페이지에 보여줄 수 있도록 하는 기능
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)